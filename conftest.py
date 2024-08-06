import os
import requests
import pytest
from dotenv import load_dotenv

load_dotenv()


try:
    HOST = "https://dev-gs.qa-playground.com/api/v1" if os.environ["STAGE"] == "qa" \
        else "https://release-gs.qa-playground.com/api/v1"
except KeyError:
    HOST = "https://release-gs.qa-playground.com/api/v1"



@pytest.fixture(autouse=False, scope="session")
def init_environment():
    response = requests.post(
        f"{HOST}/setup",
        headers={"Authorization": f"Bearer {os.getenv('API_TOKEN')}",
                 "X-Task-Id": "API-3"
                 },

    )
    assert response.status_code == 205, f"Unexpected Response status code: {response.status_code}"
    print(response.status_code)
    print(HOST)
