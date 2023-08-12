import requests

from .main import AbstractSMSModule


class MagfaSMSModule(AbstractSMSModule):
    def __init__(self, base_url, username, password, domain):
        self.base_url = base_url
        self.auth = self._prepare_authorization_header(username, password, domain)
        self.headers = self._prepare_headers()

    def _prepare_authorization_header(self, username, password, domain):
        return f"{username}/{domain}", password

    def _prepare_headers(self):
        return {
            "accept": "application/json",
            "cache-control": "no-cache",
        }

    def send_message(self, cellphone: str, message: str) -> str:
        url = f"{self.base_url}/send"
        payload_json = {
            "senders": ["30007510"],
            "messages": [message],
            "recipients": [cellphone],
        }
        response = requests.post(url, headers=self.headers, auth=self.auth, json=payload_json)

        return response.json()
