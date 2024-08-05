

class ApplicationError(Exception):
    def __init__(self, details: str, *args: object) -> None:
        self.details = details
        super().__init__(*args)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(details='{self.details}')"
