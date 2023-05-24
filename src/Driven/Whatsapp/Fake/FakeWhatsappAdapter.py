from src.Port.LogPort import LogPort
from src.Port.WhatsappPort import WhatsappPort

class FakeWhatsappAdapter(WhatsappPort):
    def __init__(self, account_sid: str, auth_token: str, logger: LogPort) -> None:
        self.__account_sid = account_sid
        self.__auth_token = auth_token
        self.__logger = logger
    
    def send_message(self, message: str) -> None:
        self.__logger.info(message='key=fake-whatsapp-request action=send_message_init')
        
        self.__logger.critical(message=f'key=fake-whatsapp-api-client action=show account_sid={self.__account_sid} auth_token={self.__auth_token}')
        
        self.__logger.info(message='key=fake-whatsapp-response action=send_message_end')