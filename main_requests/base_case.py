import json.decoder
from datetime import datetime
from requests import Response
from main_requests.base_assertion import Assertion
from main_requests.api_client import APIClient


def find_all_keys(d, key):
    values = []
    if key in d:
        values.append(d[key])
    for k, v in d.items():
        if isinstance(v, dict):
            values.extend(find_all_keys(v, key))
        elif isinstance(v, list):
            for item in v:
                if isinstance(item, dict):
                    values.extend(find_all_keys(item, key))
    return values


class BaseCase(APIClient):

    assertion = Assertion()

    def get_cookie(self, response: Response, cookie_name):
        assert cookie_name in response.cookies, f"Cannot find cookies with name:{cookie_name} in the last request"
        return response.cookies[cookie_name]

    def get_header(self, response: Response, header_name):
        assert header_name in response.headers, f"Cannot find cookies with name:{header_name} in the last request"
        return response.headers[header_name]

    def get_json_value(self, response: Response, name):
        try:
            response_dict = response.json()
        except json.decoder.JSONDecoder:
            assert False, f"The response is not in JSON format. Response text is: {response.text}"
        values = find_all_keys(response_dict, name)
        assert len(values) > 0, f"The key: {name} is not in response JSON"
        return values



