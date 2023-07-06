from abc import ABC, abstractmethod
from  src.Command.QuotationResult import QuotationResult

class QuotationProviderPort(ABC):
    @abstractmethod
    def collect(self) -> QuotationResult:
        pass