import os
from dotenv import load_dotenv

load_dotenv()


class Headers:

    admin = {
        "Authorization": f"Bearer {os.getenv('API_TOKEN_ADMIN')}",
    }
    operator = {
        "Authorization": f"Bearer {os.getenv('API_TOKEN_OPERATOR')}",
    }
