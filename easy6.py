import colorama
class Cars:
    def __init__(self, car_name=None, model = None, manufactured_year= None, price=None) -> None:
        self.car_name = car_name
        self.model = model
        self.manufactured_year = manufactured_year
        self.price = price
        
    def enter(self):
        self.car_name = input("Enter make: ")
        self.model = input("Enter model: ")
        self.manufactured_year = int(input("Enter year: "))
        self.price = float(input("Enter price: "))
    
    def printt(self):
                return f"\n{colorama.Fore.RED}Make: {colorama.Fore.CYAN}{self.car_name}\n{colorama.Fore.RED}Model: {colorama.Fore.GREEN}{self.model}\n{colorama.Fore.RED}Year: {colorama.Fore.YELLOW}{self.manufactured_year}\n{colorama.Fore.RED}price: {colorama.Fore.LIGHTMAGENTA_EX}{self.price}{colorama.Style.RESET_ALL}\n"

    
car1 = Cars("BMW", "M5", 2016, 112000.00)
cars = [car1]

print('Available cars which are made after 2010: ')
count = 0
for car in cars:
    if car.manufactured_year > 2010:
        print(car.printt())
        count += 1
        
if count == 0:
    print("Not availale yet!")
        
n = int(input("How many cars do you add: "))

for i in range(n):
    car = Cars()
    car.enter()
    cars.append(car)
    


count1 = 0
for car in cars:
    if car.manufactured_year >= 2010:
        print(car.printt())
        count1 += 1

if count1 == 0:
    print("Not available cars which are made after 2010")
        