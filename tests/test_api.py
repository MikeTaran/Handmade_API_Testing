import pytest
import allure

from main_requests.base_case import BaseCase
from main_requests.owner.owner_requests import Owner


class TestAPI:

    @allure.feature('API Testing')
    @allure.story('Test FullRest API')
    def test_get_owner_info(self, transaction_data, formatted_date):
        owner_id = "778913"
        owner = Owner()
        base_case = BaseCase()
        transaction_sum, bank_account_balance = transaction_data
        date_short, date_long, cur_time = formatted_date

        response = owner.get_owner_info(owner_id)
        assert response.status_code == 200, f"Expected status code 201, but got {response.status_code}"
        print(response.status_code)
        print(response.json())
        status = base_case.get_json_value(response, "id")
        print(status)
