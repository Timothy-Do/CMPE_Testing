# Homework
- Name: Timothy Do

## Question 1) Define the following unit, integration, regression tests and when you would use each?
- A unit test, tests a single function or component in isolation in order to ensure it works as expected. You would use it during development to catch any small bugs early.
- An integration test, tests how different modules or components work together. You would use it after unit tests to verify that combined parts interact correctly.
- A regression test ensures that recent code changes haven't broken existing functionalities. You would use it after bug fixes or feature updates in order to maintain stability.

## Question 2) Briefly explain pytest discovery (file/function naming) and what a fixture is.
- Pytest discovery is a mechanism that automatically identifies and runs tests by searching for files named `test_*.py` or `*_test.py`, and functions that begin with the prefix `test_`.
- A fixture is a function defined with the `@pytest.fixture` decorator that provides a consistent and reusable setup or resource for tests before they are executed.
