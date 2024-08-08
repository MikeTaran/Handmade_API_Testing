from main_requests.base_case import BaseCase
from config.endpoints import Endpoints
from config.headers import Headers


class Owner(BaseCase):

    def get_owner_info(self, owner_id):

        uri = Endpoints.owner_info_uri(owner_id)
        response = self.get(uri, headers=Headers.admin)
        self.assertion.assert_response_code_status(response, 200)
        return response

    def set_owner_status(self, owner_id):
        pass
