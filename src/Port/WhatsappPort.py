from abc import ABC, abstractmethod

class WhatsappPort(ABC):
    @abstractmethod
    def send_message(self, message: str) -> None:
        pass