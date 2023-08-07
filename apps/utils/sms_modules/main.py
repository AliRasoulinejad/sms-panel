from abc import ABC, abstractmethod


class AbstractSMSModule(ABC):
    @abstractmethod
    def _prepare_authorization_header(self, username, password, domain) -> str:
        raise NotImplementedError

    @abstractmethod
    def _prepare_headers(self) -> dict:
        raise NotImplementedError

    @abstractmethod
    def send_message(self, cellphone: str, message: str) -> str:
        raise NotImplementedError
