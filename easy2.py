import colorama

class Employe:
    def __init__(self, full_name, income) -> None:
        self.full_name = full_name
        self.income = income
    
    def yearly_income(self):
        return f"Yearly income of {colorama.Fore.YELLOW}{self.full_name}{colorama.Style.RESET_ALL} is {colorama.Fore.BLUE}{self.income * 12}{colorama.Style.RESET_ALL}"

worker1 = Employe("Ali Valiyev", 500)
worker2 = Employe("Eldor Shomrodov", 700)
worker3 = Employe("Amir Ikramov", 1000)

workers = [worker1, worker2, worker3]

for worker in workers:
    print(worker.yearly_income())