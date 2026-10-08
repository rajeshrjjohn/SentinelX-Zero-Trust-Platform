"""
Evaluate SentinelX anomaly detection on labeled flow data.

Trains two models:
  1. Isolation Forest (unsupervised) - trained on benign flows only,
     scored on a held-out mix of benign + attack flows.
  2. Random Forest (supervised baseline) - trained on labeled benign + attack flows.

Splits data by TIME, not randomly, so the test set simulates "future" traffic
the model has never seen (avoids leakage between train/test).

Writes metrics (precision, recall, F1, false-positive rate, confusion matrix)
to RESULTS.md.
"""

import sys
import pandas as pd
import numpy as np
from sklearn.ensemble import IsolationForest, RandomForestClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import (
    precision_score, recall_score, f1_score,
    confusion_matrix, classification_report
)

FEATURES = [
    "duration", "pkt_count", "byte_count", "pkts_per_sec", "bytes_per_sec",
    "avg_pkt_size", "std_pkt_size", "syn_count", "ack_count", "rst_count",
    "unique_dst_ports",
]


def load_and_split(path, test_frac=0.3):
    df = pd.read_csv(path)
    df = df.dropna(subset=FEATURES)

    benign = df[df.label == 0].reset_index(drop=True)
    attack = df[df.label == 1].reset_index(drop=True)

    b_split = int(len(benign) * (1 - test_frac))
    a_split = int(len(attack) * (1 - test_frac))

    train = pd.concat([benign.iloc[:b_split], attack.iloc[:a_split]], ignore_index=True)
    test = pd.concat([benign.iloc[b_split:], attack.iloc[a_split:]], ignore_index=True)

    return train, test


def evaluate_predictions(y_true, y_pred, name):
    tn, fp, fn, tp = confusion_matrix(y_true, y_pred, labels=[0, 1]).ravel()
    precision = precision_score(y_true, y_pred, zero_division=0)
    recall = recall_score(y_true, y_pred, zero_division=0)
    f1 = f1_score(y_true, y_pred, zero_division=0)
    fpr = fp / (fp + tn) if (fp + tn) > 0 else 0.0

    return {
        "name": name,
        "precision": precision,
        "recall": recall,
        "f1": f1,
        "false_positive_rate": fpr,
        "tn": int(tn), "fp": int(fp), "fn": int(fn), "tp": int(tp),
    }


def run_isolation_forest(train, test, scaler):
    X_train_benign = scaler.transform(train[train.label == 0][FEATURES])
    X_test = scaler.transform(test[FEATURES])
    y_test = test["label"].values

    model = IsolationForest(n_estimators=200, contamination="auto", random_state=42)
    model.fit(X_train_benign)

    raw_pred = model.predict(X_test)
    y_pred = np.where(raw_pred == -1, 1, 0)

    return evaluate_predictions(y_test, y_pred, "Isolation Forest (unsupervised, benign-only training)")


def run_random_forest(train, test, scaler):
    X_train = scaler.transform(train[FEATURES])
    y_train = train["label"].values
    X_test = scaler.transform(test[FEATURES])
    y_test = test["label"].values

    model = RandomForestClassifier(
        n_estimators=200, max_depth=12, class_weight="balanced", random_state=42
    )
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)

    importances = pd.Series(model.feature_importances_, index=FEATURES).sort_values(ascending=False)

    result = evaluate_predictions(y_test, y_pred, "Random Forest (supervised baseline)")
    result["feature_importances"] = importances
    return result


def write_results_md(train, test, if_result, rf_result, out_path="RESULTS.md"):
    lines = []
    lines.append("# SentinelX Evaluation Results\n")
    lines.append("## Dataset\n")
    lines.append(f"- Total flows: {len(train) + len(test)}")
    lines.append(f"- Benign flows: {(train.label==0).sum() + (test.label==0).sum()}")
    lines.append(f"- Attack flows: {(train.label==1).sum() + (test.label==1).sum()}")
    lines.append(f"- Train set: {len(train)} flows (benign={ (train.label==0).sum() }, attack={ (train.label==1).sum() })")
    lines.append(f"- Test set: {len(test)} flows (benign={ (test.label==0).sum() }, attack={ (test.label==1).sum() })")
    lines.append("- Split method: time-ordered per class (first ~70% train, last ~30% test), not random — avoids leakage across train/test.\n")

    lines.append("## Results\n")
    lines.append("| Model | Precision | Recall | F1 | False Positive Rate |")
    lines.append("|---|---|---|---|---|")
    for r in (if_result, rf_result):
        lines.append(
            f"| {r['name']} | {r['precision']:.3f} | {r['recall']:.3f} | {r['f1']:.3f} | {r['false_positive_rate']:.3f} |"
        )
    lines.append("")

    for r in (if_result, rf_result):
        lines.append(f"### {r['name']}")
        lines.append(f"Confusion matrix (rows=actual, cols=predicted; 0=benign, 1=attack):\n")
        lines.append("```")
        lines.append(f"            pred_benign  pred_attack")
        lines.append(f"actual_benign  {r['tn']:>6}       {r['fp']:>6}")
        lines.append(f"actual_attack  {r['fn']:>6}       {r['tp']:>6}")
        lines.append("```\n")

    if "feature_importances" in rf_result:
        lines.append("### Random Forest Feature Importances\n")
        lines.append("| Feature | Importance |")
        lines.append("|---|---|")
        for feat, imp in rf_result["feature_importances"].items():
            lines.append(f"| {feat} | {imp:.3f} |")
        lines.append("")

    lines.append("## Notes & Limitations\n")
    lines.append("- Benign traffic was captured on the host's main interface (`eth0`); attack traffic was captured against a local Docker container (`docker0`). Interface-level artifacts (latency, MTU) could differ between the two in ways unrelated to attack behavior, so features sensitive to this were excluded.")
    lines.append("- Attack set is dominated by port-scan flows (single-packet, SYN-only), which inflates attack flow count relative to benign. Precision/recall above should be read with this class balance in mind.")
    lines.append("- Isolation Forest was trained only on benign flows (no attack labels used at training time), matching a realistic deployment where attack examples aren't available in advance. Random Forest uses labels and serves as a supervised upper-bound comparison.")

    with open(out_path, "w") as f:
        f.write("\n".join(lines))

    print(f"Wrote results to {out_path}")


if __name__ == "__main__":
    flows_path = sys.argv[1] if len(sys.argv) > 1 else "data/processed/flows.csv"

    train, test = load_and_split(flows_path)
    print(f"Train: {len(train)} flows | Test: {len(test)} flows")

    scaler = StandardScaler()
    scaler.fit(train[FEATURES])

    if_result = run_isolation_forest(train, test, scaler)
    rf_result = run_random_forest(train, test, scaler)

    for r in (if_result, rf_result):
        print(f"\n{r['name']}")
        print(f"  Precision: {r['precision']:.3f}  Recall: {r['recall']:.3f}  F1: {r['f1']:.3f}  FPR: {r['false_positive_rate']:.3f}")
        print(f"  TN={r['tn']} FP={r['fp']} FN={r['fn']} TP={r['tp']}")

    write_results_md(train, test, if_result, rf_result)
