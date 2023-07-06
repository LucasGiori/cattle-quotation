from src.Model import Price, Location, Variation, Date

class Quotation:
    def __init__(self, location: Location, reference_date: Date, current: Price, future: Price, current_without_funrural: Price, future_without_funrural: Price, variation: Variation = None) -> None:
        self.location = location
        self.reference_date = reference_date
        self.current = current
        self.future = future
        self.current_without_funrural = current_without_funrural
        self.future_without_funrural = future_without_funrural
        self.variation = variation

    def to_dict(self) -> dict:
        return {
            'location': self.location.getValue(),
            'reference_date': self.reference_date.getValue(),
            'current': self.current.getValue(),
            'future': self.future.getValue(),
            'current_without_funrural': self.current_without_funrural.getValue(),
            'future_without_funrural': self.future_without_funrural.getValue(),
            'variation': self.variation.getValue()
        }