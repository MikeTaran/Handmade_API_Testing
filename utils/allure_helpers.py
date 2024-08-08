import allure
import json
from allure_commons.types import AttachmentType


class Helper:

    def attach_response(self, response):
        response = json.dumps(response, indent=4, ensure_ascii=False)
        allure.attach(body=response, name="API Response", attachment_type=AttachmentType.JSON)

# allure_helper.attach_response(response.json())
    def step(self, description):
        def wrapper(func):
            def wrapped(*args, **kwargs):
                with allure.step(description):
                    return func(*args, **kwargs)
            return wrapped
        return wrapper
