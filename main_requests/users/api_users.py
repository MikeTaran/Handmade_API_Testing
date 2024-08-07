import allure
import requests

from config.headers import Headers
from config.endpoints import Endpoints
from main_requests.users.pyloads import Payloads
from utils.helper import Helper
from main_requests.users.models.user_model import UserModel


class UsersAPI(Helper):
    def __init__(self):
        super().__init__()
        self.payloads = Payloads()
        self.endpoints = Endpoints()
        self.headers = Headers()

    @allure.step("Create User")
    def create_user(self):
        response = requests.post(
            url=self.endpoints.create_user,
            headers=self.headers.basic,
            json=self.payloads.create_user
        )
        # print(response.json())
        assert response.status_code == 200, response.json()
        self.attach_response(response.json())
        model = UserModel(**response.json())
        return model

    @allure.step("Get user by ID")
    def get_user_by_id(self, uuid):
        response = requests.get(
            url=self.endpoints.get_user_by_id(uuid),
            headers=self.headers.basic,
        )
        # print(response.json())
        assert response.status_code == 200, response.json()
        self.attach_response(response.json())
        model = UserModel(**response.json())
        return model
