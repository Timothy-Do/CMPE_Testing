import pytest
from order_io import load_order

def test_load_order_malformed_line_raises(tmp_path):
    p = tmp_path / "bad.csv"
    p.write_text("ok,$1.00\nbadline\n", encoding="utf-8")
    with pytest.raises(ValueError):
        load_order(p)
