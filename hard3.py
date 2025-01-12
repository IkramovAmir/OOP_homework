class Manager:
    def __init__(self, name, lavozim, time, income) -> None:
        self.name = name
        self.lavozim = lavozim
        self.time = time
        self.income = income
        
    def filter_Manager(self):
        if self.time < 40 and self.lavozim != "Rahbar":
            workers.remove(self)

worker1 = Manager("Hamdam", "Rahbar", 45, 1200000)
worker2 = Manager("Damdam", "Kotib", 35, 700000)
worker3 = Manager("Zarrux", "Rahbar", 41, 14000000)
worker4 = Manager("Amir", "Rahbar", 40, 500000)
worker5 = Manager("ali", "Rahbar", 50, 100000)
worker6 = Manager("Vali", "ustoz", 20, 50000000)
worker7 = Manager("Kimdir", "Rahbar", 40, 20000000)
workers = [worker1, worker2, worker3, worker4, worker5, worker6, worker7]

for worker in workers[:]:  
    worker.filter_Manager()


for worker in workers:
     print(f"{worker.name} - {worker.lavozim} - {worker.time} hours - {worker.income}")