from pricing import apply_discount

def test_apply_discount_regression():
    """
    Regression test for the known bug: apply_discount treats 'percent'
    as a raw multiplier instead of percent/100.

    Correct behavior for 10% off of 100.0 should be 90.0.
    This test should FAIL until the bug is fixed.
    """
    result = apply_discount(100.0, 10)   # expecting 10% discount
    assert result == 90.0
