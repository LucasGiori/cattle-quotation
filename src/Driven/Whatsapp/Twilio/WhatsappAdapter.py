from twilio.rest import Client
from src.Port.LogPort import LogPort
from src.Port.WhatsappPort import WhatsappPort

class WhatsappAdapter(Client, WhatsappPort):
    def __init__(self, account_sid: str, auth_token: str, logger: LogPort) -> None:
        super().__init__(account_sid, auth_token)
        self.__logger = logger
    
    def send_message(self, message: str) -> None:
        self.__logger.info(message='key=twilio-request action=send_message_init')

        message = super().messages.create(from_='whatsapp:+14155238886', body=message, to='whatsapp:+556993370285')
        
        self.__logger.info(message=f'key=twilio-response action=send_message_end response={message.sid}')