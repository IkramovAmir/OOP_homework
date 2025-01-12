class Instruments:
    def __init__(self, name, price, company, type) -> None:
        self.name = name
        self.price = price
        self.company = company
        self.type = type
        
    def filter_klaviatura(self):
        if self.price > 2000000 and self.type == "klaviatura":
            print(f"{self.name} | {self.price} | {self.company} | {self.type}")

instrument1 = Instruments("piano", 2900000, "apple", "klaviatura")
instrument2 = Instruments("radio", 1200000, "samsung", "stuna")
instrument3 = Instruments("other", 1200000, "redmi", "B")
instrument4 = Instruments("Theother", 2200000, "google", "klaviatura")
instrument5 = Instruments("piano", 1200000, "apple", "N")
instrument6 = Instruments("comp", 1200000, "apple", "klaviatura")
instrument7 = Instruments("piano", 2200000, "apple", "klaviatura")
instruments = [instrument1, instrument2, instrument3, instrument4, instrument5, instrument6, instrument7]


for instrument in instruments:
    instrument.filter_klaviatura()