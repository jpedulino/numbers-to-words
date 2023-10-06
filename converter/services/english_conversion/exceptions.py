class ConversionLimitExceeded(Exception):
    def __init__(self) -> None:
        self.message = "Conversion limit was exceeded. Please enter a value that has 24 digits or less."
        super().__init__(self.message)
