from tests.test_data import generate_transaction_data, format_date
import pytest


@pytest.fixture(scope='function')
def transaction_data():
    return generate_transaction_data()


@pytest.fixture(scope='function')
def formatted_date():
    return format_date()
