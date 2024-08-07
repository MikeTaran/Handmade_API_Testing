import json

import requests
from config.endpoints import Endpoints
from config.headers import Headers
from main_requests.base_assertion import Assertion
from main_requests.base_case import BaseCase
from main_requests.base_methods import MyRequests


def find_key(d, key):
    if key in d:
        return d[key]
    for k, v in d.items():
        if isinstance(v, dict):
            result = find_key(v, key)
            if result is not None:
                return result
        elif isinstance(v, list):
            for item in v:
                if isinstance(item, dict):
                    result = find_key(item, key)
                    if result is not None:
                        return result
    return None


class TestOwner(BaseCase):
    def test_get_owner_info(self):

        endpoint = Endpoints()

        uuid = 778913
        header = Headers.admin
        url = endpoint.get_owner_info(uuid)
        response = MyRequests.get(url, headers=header)
        print(response.status_code)
        print(response.text)
        Assertion.assert_response_code_status(response, 200)
        owner_data = self.get_json_value(response, "data")
        data = response.json()
        owner_status = find_key(data, "status")
        print(owner_status)