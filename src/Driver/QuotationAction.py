from flask import jsonify, make_response
from src.Config.Container import Container
from src.Port.QuotationProviderPort import QuotationProviderPort
from src.Config.Container import Container
from src.Command.QuotationCommandHandler import QuotationCommandHandler

def quotation_action(container: Container):
    command_handler = QuotationCommandHandler(quotation_port=container.get(QuotationProviderPort))
    quotation_result = command_handler.execute()
    
    response = jsonify([quotation.to_dict() for quotation in quotation_result.getValue()])
    # response.headers['Content-Type'] = 'application/json'
    
    return make_response(response, 201)