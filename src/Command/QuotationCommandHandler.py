from src.Port.QuotationProviderPort import QuotationProviderPort
from src.Command.QuotationResult import QuotationResult


class QuotationCommandHandler:
    def __init__(self, quotation_port: QuotationProviderPort) -> None:
        self._quotation_port = quotation_port
        
    def execute(self) -> QuotationResult:
        return self._quotation_port.collect()