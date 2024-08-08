import os

try:
    HOST = "https://api.loki.dev.websitewizard.ru" if os.environ["STAGE"] == "loki" \
        else "https://websitewizard.ru"
except KeyError:
    HOST = "https://websitewizard.ru"