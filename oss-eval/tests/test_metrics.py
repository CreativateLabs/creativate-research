from evalkit.metrics import mae, smape

def test_mae():
    assert mae([1,2,3],[1,2,3]) == 0

def test_smape_zero():
    assert smape([0,0],[0,0]) == 0
