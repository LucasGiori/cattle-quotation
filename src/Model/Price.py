class Price:
    def __init__(self, value: float) -> None:
        self.__validate(value)

        self.value = value
        

    def __validate(self, value: str) -> None:
        if(not value):
            raise ValueError('Price invalid')
        
    def getValue(self) -> str:
        return self.value