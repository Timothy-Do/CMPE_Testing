import pytest
from pricing import parse_price, format_currency, apply_discount, add_tax, bulk_total

# parse_price
@pytest.mark.parametrize("raw, expected", [
    ("$1,234.50", 1234.5),
    ("12.5", 12.5),
    (" $0.99 ", 0.99),
])
def test_parse_price_valid(raw, expected):
    assert parse_price(raw) == expected

@pytest.mark.parametrize("raw", [
    "",
    "abc",
    pytest.param("$12,34,56", marks=pytest.mark.xfail(
        reason="Known bug: comma grouping not validated", strict=True)),
])
def test_parse_price_invalid(raw):
    with pytest.raises(ValueError):
        parse_price(raw)

# format_currency
@pytest.mark.parametrize("value, expected", [
    (0, "$0.00"),
    (2.2, "$2.20"),
])
def test_format_currency(value, expected):
    assert format_currency(value) == expected

# apply_discount
def test_apply_discount_zero_ok():
    assert apply_discount(100.0, 0) == 100.0

def test_apply_discount_negative_raises():
    with pytest.raises(ValueError):
        apply_discount(10.0, -1)

@pytest.mark.xfail(reason="Known bug: percent should be divided by 100", strict=True)
def test_apply_discount_ten_percent():
    assert apply_discount(100.0, 10) == 90.0

# add_tax
def test_add_tax_default_rate():
    assert add_tax(100.0) == pytest.approx(107.0)

def test_add_tax_negative_rate_raises():
    with pytest.raises(ValueError):
        add_tax(10.0, rate=-0.01)

# bulk_total
def test_bulk_total_simple_list():
    # 10 + 10 = 20
    # 7% tax --> 21.4
    assert bulk_total([10, 10]) == pytest.approx(21.4)
