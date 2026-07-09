def calculate_trust_score(
    anomaly,
    packet_length
):

    trust = 100

    if anomaly:
        trust -= 50

    if packet_length > 1000:
        trust -= 20

    if trust < 0:
        trust = 0

    return trust
