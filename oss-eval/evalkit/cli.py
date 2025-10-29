import argparse, json
from .metrics import mae, smape

def main():
    p = argparse.ArgumentParser(description="Simple eval CLI")
    p.add_argument("--y_true", type=str, required=True, help="JSON list, e.g. [1,2,3]")
    p.add_argument("--y_pred", type=str, required=True, help="JSON list, e.g. [1.1,2.2,3.3]")
    args = p.parse_args()
    y_true = json.loads(args.y_true)
    y_pred = json.loads(args.y_pred)
    print(json.dumps({"mae": mae(y_true, y_pred), "smape": smape(y_true, y_pred)}))
