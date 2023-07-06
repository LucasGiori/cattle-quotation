class Date:
    def __init__(self, value: str) -> None:
        self.__validate(value)

        self.value = value
        

    def __validate(self, value: str) -> None:
        if(not value):
            raise ValueError('Date invalid')
        
    def getValue(self) -> str:
        return self.value