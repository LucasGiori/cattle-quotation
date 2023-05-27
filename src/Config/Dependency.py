from src.Config.Container import Container
from src.Port.LogPort import LogPort
from src.Port.WhatsappPort import WhatsappPort
from src.Port.QuotationProviderPort import QuotationProviderPort
from src.Driven.Log.LogAdapter import LogAdapter
from src.Driven.Quotation.ScotConsultoria.FatOxAdapter import FatOxAdapter
from src.Driven.Whatsapp.Fake.FakeWhatsappAdapter import FakeWhatsappAdapter
from src.Driven.Whatsapp.Twilio.WhatsappAdapter import WhatsappAdapter
from src.Config.Environment import Environment
from requests import Session

class Dependency:
    @staticmethod
    def register_default(container: Container):
        container.register(key=LogPort, dependency=LogAdapter)
        # container.register(
        #     key=WhatsappPort, 
        #     dependency=FakeWhatsappAdapter(
        #         account_sid=Environment.get('FAKE_ACCESS_ID'), 
        #         auth_token=Environment.get('FAKE_AUTH_TOKEN'),
        #         logger=container.get(key=LogPort)
        #     )
        # )
        container.register(
            key=WhatsappPort, 
            dependency=lambda: WhatsappAdapter(
                account_sid=Environment.get('TWILIO_ACCESS_ID'), 
                auth_token=Environment.get('TWILIO_AUTH_TOKEN'),
                logger=container.get(key=LogPort)
            )
        )
        container.register(
            key=QuotationProviderPort, 
            dependency=FatOxAdapter(
                session=Session(), 
                logger=container.get(key=LogPort)
            )
        )