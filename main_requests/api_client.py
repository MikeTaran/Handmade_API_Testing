import allure
import requests
from config.environment import HOST
from utils.allure_helpers import Helper


class APIClient:
    def __init__(self):
        self.base_url = HOST

    @staticmethod
    def get(uri: str, data: dict = None, headers: dict = None, cookies: dict = None, ):
        with allure.step(f"GET request to URL: {uri}"):
            return APIClient._send(uri, data, headers, cookies, "GET")

    @staticmethod
    def post(uri: str, data: dict = None, headers: dict = None, cookies: dict = None, ):
        with allure.step(f"POST request to URL: {HOST}{uri}"):
            return APIClient._send(uri, data, headers, cookies, "POST")

    @staticmethod
    def put(uri: str, data: dict = None, headers: dict = None, cookies: dict = None, ):
        with allure.step(f"PUT request to URL: {HOST}{uri}"):
            return APIClient._send(uri, data, headers, cookies, "PUT")

    @staticmethod
    def delete(uri: str, data: dict = None, headers: dict = None, cookies: dict = None, ):
        with allure.step(f"DELETE request to URL: {HOST}{uri}"):
            return APIClient._send(uri, data, headers, cookies, "DELETE")

    @staticmethod
    def _send(uri: str, data: dict, headers: dict, cookies: dict, method: str):
        url = f"{HOST}{uri}"
        if headers is None:
            headers = {}
        if cookies is None:
            cookies = {}
        allure_helper = Helper()
        # Logger.add_request(url, data, headers, cookies, method)
        if method == "GET":
            response = requests.get(url, params=data, headers=headers, cookies=cookies)
        elif method == "POST":
            response = requests.post(url, data=data, headers=headers, cookies=cookies)
        elif method == "PUT":
            response = requests.put(url, data=data, headers=headers, cookies=cookies)
        elif method == "DELETE":
            response = requests.delete(url, data=data, headers=headers, cookies=cookies)
        else:
            raise Exception(f"Bad HTTP method:{method} was received")
        # Logger.add_response(response)
        allure_helper.attach_response(response.json())
        return response
