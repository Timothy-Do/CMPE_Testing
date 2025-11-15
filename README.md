# Homework
- Name: Timothy Do

## Question 1) Define the following unit, integration, regression tests and when you would use each?
- A unit test, tests a single function or component in isolation in order to ensure it works as expected. You would use it during development to catch any small bugs early.
- An integration test, tests how different modules or components work together. You would use it after unit tests to verify that combined parts interact correctly.
- A regression test ensures that recent code changes haven't broken existing functionalities. You would use it after bug fixes or feature updates in order to maintain stability.

## Question 2) Briefly explain pytest discovery (file/function naming) and what a fixture is.
- Pytest discovery is a mechanism that automatically identifies and runs tests by searching for files named `test_*.py` or `*_test.py`, and functions that begin with the prefix `test_`.
- A fixture is a function defined with the `@pytest.fixture` decorator that provides a consistent and reusable setup or resource for tests before they are executed.

## Question 3) What pytest features were used in the unit tests?

- **@pytest.mark.parametrize** — used to test multiple input/output pairs in a single test function for cleaner and more efficient testing
- **pytest.raises** — used to verify that functions raise expected exceptions
- **pytest.mark.xfail** — used to mark known bugs or expected failures without breaking the entire test suite
- **pytest.approx** — used for comparing floating-point numbers that may have small rounding differences

These features helped create concise, organized, and maintainable unit tests for all five functions (`parse_price`, `format_currency`, `apply_discount`, `add_tax`, and `bulk_total`).
