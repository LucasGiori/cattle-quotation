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
from bs4 import BeautifulSoup
from typing import List
import re

class FatOxAdapter(QuotationProviderPort):
    PATH = 'https://www.scotconsultoria.com.br/cotacoes/boi-gordo'
    def __init__(self, session: Session, logger: LogPort) -> None:
        self.__session = session
        self.__logger = logger

    
    def collect(self)-> QuotationResult: 
        self.__logger.info(message='key=http-request action=scraping_init')
        
        result = self.__session.get(url=self.PATH)
        
        self.__logger.info(message=f'key=http-response action=scraping_end status_code={result.status_code}')
        
        return QuotationResult(quotation_list=self.__extract(html=result))
        
    
    def __extract(self, html) -> List[Quotation]:
        soup = BeautifulSoup(html.text, 'html.parser')

        tables = soup.find_all('table')

        metadata = tables[1]

        pattern = r'\d{2}/\d{2}/\d{4}'
        match = re.search(pattern, metadata.find('thead').text)

        reference_date = match.group() if match is not None else '--/--/----'

        quotation_brazil = tables[1]
    
        tr_elements = quotation_brazil.find('tbody').find_all('tr', class_='conteudo')
     
        quotation_list = []
        
        for tr in tr_elements:
            td = tr.find_all('td')

            quotation_list.append(
                Quotation(
                    location=Location(td[0].text),
                    reference_date=Date(reference_date),
                    current=Price(td[1].text),
                    future=Price(td[3].text),
                    current_without_funrural=Price(td[6].text),
                    future_without_funrural=Price(td[8].text),
                    variation=Variation(td[5].text)
                )
            )
        
        return quotation_list