# Eval Toolkit

Install & test:
```bash
cd oss-eval
pip install -e .
pytest -q
```

CLI example:
```bash
evalkit --y_true "[1,2,3]" --y_pred "[1.1,2.2,3.0]"
```
