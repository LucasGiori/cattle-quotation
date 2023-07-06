from src.Model.Quotation import Quotation
from typing import List
import re

class QuotationResult:
    def __init__(self, quotation_list: List[Quotation]) -> None:
        self.quotation_list = quotation_list

    def filter_by_location(self, location: str):
        pattern = re.compile(pattern=re.escape(location), flags=re.IGNORECASE)

        self.quotation_list = list(filter(lambda quotation: re.search(pattern, quotation.location.getValue()), self.quotation_list))     

    def first(self) -> Quotation:
        return self.quotation_list[0]   

    def getValue(self) -> List[Quotation]:
        return self.quotation_list