# SentinelX Evaluation Results

## Dataset

- Total flows: 22941
- Benign flows: 1058
- Attack flows: 21883
- Train set: 16058 flows (benign=740, attack=15318)
- Test set: 6883 flows (benign=318, attack=6565)
- Split method: time-ordered per class (first ~70% train, last ~30% test), not random — avoids leakage across train/test.

## Results

| Model | Precision | Recall | F1 | False Positive Rate |
|---|---|---|---|---|
| Isolation Forest (unsupervised, benign-only training) | 0.980 | 0.999 | 0.990 | 0.415 |
| Random Forest (supervised baseline) | 1.000 | 0.999 | 1.000 | 0.000 |

### Isolation Forest (unsupervised, benign-only training)
Confusion matrix (rows=actual, cols=predicted; 0=benign, 1=attack):

```
            pred_benign  pred_attack
actual_benign     186          132
actual_attack       5         6560
```

### Random Forest (supervised baseline)
Confusion matrix (rows=actual, cols=predicted; 0=benign, 1=attack):

```
            pred_benign  pred_attack
actual_benign     318            0
actual_attack       6         6559
```

### Random Forest Feature Importances

| Feature | Importance |
|---|---|
| pkts_per_sec | 0.276 |
| avg_pkt_size | 0.226 |
| bytes_per_sec | 0.158 |
| duration | 0.119 |
| rst_count | 0.091 |
| std_pkt_size | 0.051 |
| byte_count | 0.046 |
| ack_count | 0.025 |
| syn_count | 0.006 |
| pkt_count | 0.003 |
| unique_dst_ports | 0.001 |

## Notes & Limitations

- Benign traffic was captured on the host's main interface (`eth0`); attack traffic was captured against a local Docker container (`docker0`). Interface-level artifacts (latency, MTU) could differ between the two in ways unrelated to attack behavior, so features sensitive to this were excluded.
- Attack set is dominated by port-scan flows (single-packet, SYN-only), which inflates attack flow count relative to benign. Precision/recall above should be read with this class balance in mind.
- Isolation Forest was trained only on benign flows (no attack labels used at training time), matching a realistic deployment where attack examples aren't available in advance. Random Forest uses labels and serves as a supervised upper-bound comparison.