from order_io import load_order, write_receipt

def test_order_integration(tmp_path):
    # create a temp input CSV file
    input_file = tmp_path / "order.csv"
    input_file.write_text("widget,$10.00\ngizmo,5.50\n", encoding="utf-8")

    # load items and generate a receipt
    items = load_order(input_file)
    output_file = tmp_path / "receipt.txt"
    write_receipt(output_file, items, discount_percent=10, tax_rate=0.1)

    # read and verify receipt contents
    output_text = output_file.read_text(encoding="utf-8")
    assert "widget: $10.00" in output_text
    assert "gizmo: $5.50" in output_text
    assert "TOTAL:" in output_text

def test_write_receipt_total_exact(tmp_path):
    items = [("a", 10.0), ("b", 10.0)]
    out = tmp_path / "receipt.txt"
    write_receipt(out, items, discount_percent=0, tax_rate=0.07)
    txt = out.read_text(encoding="utf-8")
    assert "a: $10.00" in txt and "b: $10.00" in txt
    assert "TOTAL: $21.40" in txt
