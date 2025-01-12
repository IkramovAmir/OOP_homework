import colorama
class Phones:
    def __init__(self, name=None, ram=None, price=None, brand=None) -> None:
        self.name = name
        self.ram = ram
        self.price = price
        self.brand = brand
        
    def enter(self):
        self.name = input("Enter name of phone: ")
        self.ram = int(input("Enter ram storage of phone:"))
        self.price = float(input("Enter price of phone:"))
        self.brand = input("Enter brand of phone: ")
    
    def printt(self):
        return f"{colorama.Fore.GREEN}Name:{self.name}, {colorama.Fore.CYAN}Ram: {colorama.Fore.RED}{self.ram}, {colorama.Style.RESET_ALL}{colorama.Fore.GREEN}Price: {self.price}, Brand:{self.brand}"

phone1 = Phones("Iphone 13pro", 8, 500000, "Apple")
phone2 = Phones("Galaxy s21s", 6, 700000, "Samsung")
phone3 = Phones("Redmi ", 4, 1000000, "Brand A")
phone4 = Phones("Iphone 11", 8, 600000, "Apple")

phones = [phone1, phone2, phone3, phone4]


n_p = int(input("How many phones do u add: "))
w = []
r = range(n_p)
for i in r:
    w = Phones()
    w.enter()
    phones.append(w)
    
    
for phone in phones:
    if phone.ram > 2 and phone.ram < 8:
        print(phone.printt())