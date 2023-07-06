from src.Port.QuotationProviderPort import QuotationProviderPort
from src.Command.QuotationResult import QuotationResult
from src.Model.Quotation import Quotation
from src.Model.Location import Location
from src.Model.Price import Price
from src.Model.Date import Date
from src.Model.Variation import Variation
from src.Model.Quotation import Quotation
from src.Port.LogPort import LogPort
from requests import Session
from datetime import datetime

class FakeAdapter(QuotationProviderPort):
    def __init__(self, session: Session, logger: LogPort) -> None:
        self.__session = session
        self.__logger = logger

    
    def collect(self)-> QuotationResult: 
        self.__logger.info(message='key=http-request action=scraping_init')
        
        self.__logger.info(message=f'key=http-response action=scraping_end status_code=200')
        
        quotation_list = []
        quotation_list.append(
            Quotation(
                location=Location('PR Fake'),
                reference_date=Date(datetime.now().strftime('%d/%m/%Y')),
                current=Price('370,00'),
                future=Price('380,00'),
                current_without_funrural=Price('374,00'),
                future_without_funrural=Price('384,00'),
                variation=Variation('3,1%')
            )
        )
        
        return QuotationResult(quotation_list=quotation_list)