class Time:
    def __init__(self, hour, minute, second):
        self.hour, self.minute, self.second = hour, minute, second

class Hour:
    def __init__(self, time): 
        self.time = time
    def Increase(self): 
        self.time.hour += 5

class Minute:
    def __init__(self, time): 
        self.time = time
    def Increase(self): 
        self.time.minute += 5

class Second:
    def __init__(self, time): 
        self.time = time
    def Increase(self): 
        self.time.second += 5

time = Time(10, 15, 30)
print(f"Initial Time -> Hour: {time.hour}, Minute: {time.minute}, Second: {time.second}")

Hour(time).Increase()
Minute(time).Increase()
Second(time).Increase()

print(f"Updated Time -> Hour: {time.hour}, Minute: {time.minute}, Second: {time.second}")
