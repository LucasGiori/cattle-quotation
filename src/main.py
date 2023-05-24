from requests import Session
from src.Driven.Quotation.FakeProvider.FakeAdapter import FakeAdapter
from src.Driven.Whatsapp.Fake.FakeWhatsappAdapter import FakeWhatsappAdapter
from src.Config.Environment import Environment
from src.Driven.Log.LogAdapter import LogAdapter

def handler(event, context):    
    session = Session()
    logger = LogAdapter()
    
    adapter = FakeAdapter(session=session, logger=logger)
    
    quotation_result= adapter.collect()
    quotation_result.filter_by_location('pr')
    
    whatsappAdapter = FakeWhatsappAdapter(
        account_sid=Environment.get('FAKE_ACCESS_ID'),
        auth_token=Environment.get('FAKE_AUTH_TOKEN'),
        logger=logger
    )
    
    # Example send message 
    message = f'*Cotação Boi Gordo* \nData Referência: {quotation_result.first().reference_date.getValue()}'
    whatsappAdapter.send_message(message=message)

    for quotation in quotation_result.getValue():
        message = f"*{quotation.location.getValue()}* \nÀ Vista: *R$ {quotation.current.getValue()}*\nÀ Prazo: *R$ {quotation.future.getValue()}*\nÀ Vista Sem Funrural: *R$ {quotation.current_without_funrural.getValue()}*\nÀ Prazo Sem Funrural: *R$ {quotation.future_without_funrural.getValue()}*\nVariação de preço comparado a SP: *{quotation.variation.getValue()}*\n\n"
        whatsappAdapter.send_message(message=message)



if __name__ == '__main__':
    handler('localhost', None)