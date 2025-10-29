def mae(y_true, y_pred):
    if len(y_true) != len(y_pred):
        raise ValueError("y_true and y_pred must have same length")
    return sum(abs(a - b) for a, b in zip(y_true, y_pred)) / len(y_true)

def smape(y_true, y_pred):
    num = 0.0
    den = 0.0
    for a, b in zip(y_true, y_pred):
        num += abs(a - b)
        den += (abs(a) + abs(b)) or 1.0
    return 200.0 * num / den if den != 0 else 0.0
