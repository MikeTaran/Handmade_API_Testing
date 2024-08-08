import os


class Endpoints:
    # def __init__(self, host):
    #     self.host = HOST
    @staticmethod
    # owners
    def owner_info_uri(uuid):
        return f"/api/admin/owners/?ownerId={uuid}"
