import os

try:
    HOST = "https://api.loki.dev.websitewizard.ru" if os.environ["STAGE"] == "loki" \
        else "https://websitewizard.ru"
except KeyError:
    HOST = "https://websitewizard.ru"


class Endpoints:
    # def __init__(self, host):
    #     self.host = HOST

    # owners
    def get_owner_info(self, uuid):
        return f"{HOST}/api/admin/owners/?ownerId={uuid}"


    change_owner_status_uri = f"{HOST}/api/admin/owners/updateField"
    change_owner_status_pyload = lambda self, ownerId: {
        "ownerId": {ownerId},
        "status": 1
        # "incommingTransactionsIsAllowed":true,
        # "outcommingTransactionsIsAllowed":true
    }
