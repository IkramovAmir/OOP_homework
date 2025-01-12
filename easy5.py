import colorama
class Market:
    def __init__(self, name= None, location = None, product_type= None, work_time= None) -> None:
        self.name = name
        self.location = location
        self.product_type = product_type
        self.work_time = work_time
    
    def enter(self):
        self.name = input("\nEnter Market name: ")
        self.location = input("Enter location of market: ")
        self.product_type = input("Enter type of product: ")
        self.work_time = input("Enter data: ")
        
    def printt(self):
        return f"\n{colorama.Fore.RED}Market: {colorama.Fore.CYAN}{self.name}\n{colorama.Fore.RED}Location: {colorama.Fore.GREEN}{self.location}\n{colorama.Fore.RED}Product type: {colorama.Fore.YELLOW}{self.product_type}\n{colorama.Fore.RED}Working hours: {colorama.Fore.LIGHTMAGENTA_EX}{self.work_time}{colorama.Style.RESET_ALL}"
    
market1 = Market("Briliant Market", "Registon", "Electronics", "12:00 to 20:00")

markets = [market1]
print("Available Markets: ")
for a in markets:
    print(a.printt())

n = int(input("\nHow many infos of markets do u want to add: "))
for l in range(n):
    l= Market()
    l.enter()
    markets.append(l)
    
for a in markets:
    print(a.printt())