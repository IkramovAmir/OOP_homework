import colorama
class Restaurant:
    def __init__(self) -> None:
        pass
    
class FastFood(Restaurant):
    def __init__(self, food=None , price = None) -> None:
        self.food = food
        self.price = price
        
    def Menu_fastFood(self):
        return f"{colorama.Fore.CYAN}{self.food} {colorama.Fore.GREEN}{self.price}{colorama.Style.RESET_ALL}"
    
class FineDining(Restaurant):
    def __init__(self, food=None , price = None) -> None:
        self.food = food
        self.price = price
    
    def Menu_fineDining(self):
        return f"{colorama.Fore.CYAN}{self.food}{colorama.Style.RESET_ALL}  {colorama.Fore.GREEN}{self.price}"
        

fastfood1 = FastFood("Hot-dog", 15.000) 
fastfood2 = FastFood("Shaurma", 35.000) 
fastfood3 = FastFood("Coffee", 10.000) 
fastfood4 = FastFood("Lavash", 32.000) 
fastfood5 = FastFood("Hot-dog(2x meat)", 19.000) 
FastFoods = [fastfood1, fastfood2, fastfood3, fastfood4, fastfood5]


finedining1 = FineDining("Sushi",  49.000)
finedining2 = FineDining("Shashlik",  19.000)
finedining3 = FineDining("Osh",  40.000)
finedining4 = FineDining("Sho'rva",  30.000)
finedining5 = FineDining("Kazab kabab",  39.000)
FineDinings = [finedining1, finedining2, finedining3, finedining4, finedining5]

print(f"\n{colorama.Fore.LIGHTWHITE_EX}Restaurant: {colorama.Fore.RED}FineDining")
print(f"{colorama.Fore.YELLOW}Food    {colorama.Fore.LIGHTBLUE_EX}Prices")
for food in FineDinings:
    print(food.Menu_fineDining())
    
print(f"\n{colorama.Fore.LIGHTWHITE_EX}Restauratn: {colorama.Fore.RED}FastFood")
print(f"{colorama.Fore.YELLOW}Food    {colorama.Fore.LIGHTBLUE_EX}Prices")
for fastfood in FastFoods:
    print(fastfood.Menu_fastFood())