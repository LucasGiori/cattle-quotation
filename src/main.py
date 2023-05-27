from src.Port.WhatsappPort import WhatsappPort
from src.Port.QuotationProviderPort import QuotationProviderPort
from src.Command.QuotationCommandHandler import QuotationCommandHandler
from src.Config.Container import Container
from src.Config.Dependency import Dependency

def handler(event, context):    
    
    container = Container()
    Dependency.register_default(container=container)
    
    quotation_adapter = QuotationCommandHandler(quotation_port=container.get(QuotationProviderPort))
    quotation_result= quotation_adapter.execute()
    # quotation_result.filter_by_location('ro')
    
    whatsappAdapter = container.get(key=WhatsappPort)
    
    message = f'*Cotação Boi Gordo* \nData Referência: {quotation_result.first().reference_date.getValue()}'
    whatsappAdapter.send_message(message=message)

    for quotation in quotation_result.getValue():
        message = f"*{quotation.location.getValue()}* \nÀ Vista: *R$ {quotation.current.getValue()}*\nÀ Prazo: *R$ {quotation.future.getValue()}*\nÀ Vista Sem Funrural: *R$ {quotation.current_without_funrural.getValue()}*\nÀ Prazo Sem Funrural: *R$ {quotation.future_without_funrural.getValue()}*\nVariação de preço comparado a SP: *{quotation.variation.getValue()}*\n\n"
        whatsappAdapter.send_message(message=message)

if __name__ == '__main__':
    handler('localhost', None)