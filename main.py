# class Person:
    
#     def __init__(self, name, age, col) -> None:
#         self.name = name
#         self.age = age
#         self.col = col
        
#     def __str__(self) -> str:
#         return(f"{self.name} is {self.age} years old and his favourite color is {self.col}")
    
#     def divide(people):
#         num = sum(person.age for person in people)
#         average = num / len(people)
#         return f"Average age is {average}"

# # p1 = Person('ali', 19)
# # p2 = Person('vali', 15)
# # p3 = Person('umar', 34)

# # # persons = [p1, p2, p3]
# n = int(input("How many people do u add: "))
# r = range(1, n +1)
# people = []
# for i in r:
#     nam = input("Enter name: ")
#     age = int(input("enter age: "))
#     col = input("Enter your favourite color: ")
#     people.append(Person(nam, age, col))
    
# # print(people)
# for i in people:
#     print(i)   

# print(Person.divide(people))
    
    

# oldest = max(persons, key=lambda older: older.age)

# print(oldest)

class calculator:
    
    def __init__(self, numbers) -> None:
        self.numbers = numbers
        
    def plus(numbers):
        total = sum(num for num in numbers)
        return f"Total is {total}"
    
    def minus(numbers):
        for num in numbers:
            if numbers[0] != num:
                total -= num
            else:
                total = num
        return f"Answer is {total}"
    
    def multiply(numbers):
        total = 1
        for num in numbers:
            total *= num
        return f"multiplication of these numbers is {total}"
            
    def divide(numbers):
        total = 1
        for num in numbers:
            if num == numbers[0]:
                total = num
            else:
                total /= num
        return f"Dividation of these numbers is {total}"




def switch_case(value):
    match value:
        case 1:
            numbers = []
            a = int(input("How many numbers do u add: "))
            r = range(1, a + 1)
            for i in r:
                num = int(input("Enter number: "))
                numbers.append(num)
            print(calculator.plus(numbers))
        case 2:
            numbers = []
            a = int(input("How many numbers do u add: "))
            r = range(1, a + 1)
            for i in r:
                num = int(input("Enter number: "))
                numbers.append(num)
            print(calculator.minus(numbers))
        case 3:
            numbers = []
            a = int(input("How many numbers do u add: "))
            r = range(1, a + 1)
            for i in r:
                num = int(input("Enter number: "))
                numbers.append(num)
            print(calculator.multiply(numbers))
        case 4:
            numbers = []
            a = int(input("How many numbers do u add: "))
            r = range(1, a + 1)
            for i in r:
                num = int(input("Enter number: "))
                numbers.append(num)
            print(calculator.divide(numbers))

print("What you can do with the help of program: ", "1. You can plus numbers", "2.You can minus numbers", "3.You can multiply numbers", "4.You can divide numbers")

value = int(input("Enter number: "))
switch_case(value)
