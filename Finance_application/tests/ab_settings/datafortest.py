class DataForTestSettings:
    def __init__(self):
        self.new = {
            "theme": "white",
            "language": "russian",
            "notifications": False,
            "main_currency": "BYN"
        }

        self.new_wrong = {
            "theme": "white",
            "language": "rus",
            "notifications": False,
            "main_currency": "BYN"
        }

        self.old = {
            "theme": "auto",
            "language": "english",
            "notifications": True,
            "main_currency": "USD"
        }