# TASK1_INTERSHIP
#Exercises_covering_variables, loops, functions, OOP, lists, dictionaries, file handling, and exceptions in Python
#1_Variables and Data Types
for num in range(10):
    print(num)

#Print the sum of all even numbers from 10 to 20 
sum = 0
for i in range(2, 22, 2):
    sum = sum + i
print(sum)

#Iterate over each elemenr in list num
numbers = [1, 2, 3, 4, 5]
for i in numbers:
    # ** exponent operator
    square = i ** 2 
    print("Square of:", i, "is:", square)

#Calculate the average of list of numbers

sum = 0
for i in numbers:
    sum = sum + i
list_size = len(numbers)
average = sum / list_size
print(average)

#Practicing input(), type conversion, and f-string
name = input("What's your name? ")
age = int(input("How old are you? "))
print(f"Hi {name}, next year you'll turn {age + 1}")

#Separate integer and decimal parts
number = float(input("Enter a decimal number: "))
integer_part = int(number)
decimal_part = number - integer_part 
print(f"Integer part: {integer_part}, decimal part: {decimal_part}")

#Swap variables without a helper variable
a = 5
b = 10
a, b = b, a
print(a, b) 

#Temperature conversion
celsius = float(input("Enter the temperature in Celsius: "))
fahrenheit = celsius * 9/5 + 32
kelvin = celsius + 273.15
print(f"Fahrenheit: {fahrenheit}, Kelvin: {kelvin}")

#Check if a text is a number
text = input("Enter a number: ")
if text.isdigit():
    number = int(text)
else:
    print("That's not a valid number")

#Area and perimeter of a circle
import math

radius = float(input("Enter the circle's radius: "))
area = math.pi * radius ** 2
perimeter = 2 * math.pi * radius
print(f"Area: {area:.2f}, Perimeter: {perimeter:.2f}")


#Concatenate and count characters
first_name = input("First name: ")
last_name = input("Last name: ")
full_name = first_name + " " + last_name
print(f"Full name: {full_name}")
print(f"Character count: {len(full_name)}")

#2_LOOPS
#FizzBuzz
for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)

#Sum and average until the user types "done"
numbers = []
while True:
    entry = input("Enter a number (or 'done' to stop): ")
    if entry.lower() == "done":
        break
    numbers.append(float(entry))

if numbers:
    total = sum(numbers)
    average = total / len(numbers)
    print(f"Sum: {total}, Average: {average}")
else:
    print("No numbers were entered")

#Check if a number is prime
n = int(input("Enter a number:  "))
is_prime = n > 1
for i in range(2, int(n**0.5) + 1):
    if n % i == 0:
        is_prime = False
        break
print(f"{n} is {'prime' if is_prime else 'not prime'}")

#Multiplication table
n = int(input("Enter a number: "))
for i in range(1, 13):
    print(f"{n} x {i} = {n * i}")

#Fibonacci sequence
n = int(input("How many Fibonacci terms do you want?"))
a, b = 0, 1
for _ in range(n):
    print(a, end=" ")
    a, b = b, a + b

#Pyramid of asterisks 
height = int(input("Enter the pyramid's height: "))
for i in range(1, height + 1):
    spaces = " " * (height - i)
    stars = "*" * (2 * i - 1)
    print(spaces + stars)

#Sum the digits of a number
n = int(input("Enter an integer: "))
total = 0
while n > 0:
    digit = n % 10 
    total += digit 
    n //= 10
print(f"The sum of the digits is: {total}")

#3_Functions
#Check if a number is even
def is_even(n):
    return n % 2 == 0
print(is_even(4), is_even(7))

#Factorial (recursion)
def factorial(n):  
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)
print(factorial(5)) 

#Count vowels
def count_vowels(text):
    vowels = "aeiouAEIOU"
    return sum(1 for letter in text if letter in vowels)
print(count_vowels("Programming is Python"))

#Check if a word is a palindrome
def is_palindrome(word):
    word = word.lower().replace(" ", "")
    return word == word[::-1]
print(is_palindrome("racecar")) # True
print(is_palindrome("python")) # False

#Convert a list of temperatures
def celsius_to_fahrenheit(c):
    return c * 9/5 + 32
temperatures = [0, 10, 20, 30, 100]
converted = [celsius_to_fahrenheit(t) for t in temperatures]
print(converted)

#Calculator function
def calculator(a, b, operation):
    if operation == "add":
        return a + b
    elif operation == "subtract":
        return a - b
    elif operation == "multiply":
        return a * b
    elif operation == "divide":
        if b == 0:
            return "Error: cannot divide by zero"
        return a / b
    else:
        return "Unrecognized operation"
print(calculator(10, 5, "add"))
print(calculator(10, 0, "divide"))

#Filter even numbers from a list 
def filter_even(numbers):
    return [n for n in numbers if n % 2 == 0]
print(filter_even([1, 2, 3, 4, 5, 6])) # [2, 4, 6]

#4_Lists
#Manuel max, min, and average
numbers = [4, 8, 1, 9, 3]
maximum = numbers[0]
minimum = numbers[0]
total = 0
for n in numbers:
    if n > maximum:
        maximum = n
        if n < minimum:
            minimum = n
            total += n
            average = total / len(numbers)
            print(f"Max: {maximum}, Min: {minimum}, Average: {average}")

#Remove duplicates while keeping order
def remove_duplicates(lst):
    result = []
    for item in lst:
        if item not in result:
            result.append(item)
    return result
print(remove_duplicates([1, 2, 2, 3, 1, 4]))

#Reverse a list manually
def reverse_list(lst):
    reversed_list = []
    for i in range(len(lst) - 1, -1, -1):
        reversed_list.append(lst[i])
        return reversed_list
print(reverse_list([1, 2, 3, 4])) # [4, 3, 2, 1]

#Sort by different criteria
names = ["Carla", "Ana", "Bruno", "Zoe"]
alphabetical_order = sorted(names)
length_order = sorted(names, key=len)
print("Alphabetical:", alphabetical_order)
print("By length:", length_order)

#Combine two lists into pairs
def combine_lists(list1, list2):
    pairs = []
    for i in range(min(len(list1), len(list2))):
        pairs.append((list1[i], list2[i]))
    return pairs

print(combine_lists([1, 2, 3], ["a", "b", "c"]))

#Bubble sort
def bubble_sort(lst):
    n = len(lst)
    for i in range(n):
        for j in range(n - i - 1):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
                return lst
print(bubble_sort([5, 2, 9, 1, 5, 6]))


#Linear search
def find_element(lst, target):
    for index, value in enumerate(lst):
        if value == target:
            return index
        return -1
print(find_element([10, 20, 30, 40], 30)) # 2
print(find_element([10, 20, 30, 40], 99))

#5_Dictionaries
#Count words in a text
text = "the dog runs and the cat sleeps and the dog barks"
words = text.split()
count = {}
for word in words:
    count[word] = count.get(word, 0) + 1
print(count)

#Most expensive and cheapest product
products = {"pencil": 0.5, "notebook": 3.2, "backpack": 25.0, "eraser": 0.3}
most_expensive = max(products, key=products.get)
cheapest = min(products, key=products.get)
print(f"Most expensive: {most_expensive} (${products[most_expensive]})")
print(f"Cheapest: {cheapest} (${products[cheapest]})")

#Merge two dictionaries, summing repeated values
dict1 = {"a": 1, "b": 2, "c": 3}
dict2 = {"b": 10, "c": 5, "d": 7}
merged = dict1.copy()
for key, value in dict2.items():
    merged[key] = merged.get(key, 0) + value
print(merged) # {'a': 1, 'b': 12, 'c': 8,'d': 7 }

#Invert a dictionary
def invert_dictionary(d):
    inverted = {}
    for key, value in d.items():
        inverted.setdefault(value, []).append(key)
        return inverted
original = {"a": 1, "b": 2, "c": 1}
print(invert_dictionary(original)) 

#Average grade per student
grades = {
    "Ana": [8, 9, 7],
    "Luis": [6, 5, 7],
    "Marta": [10, 9, 10]
}
for student, scores in grades.items():
    average = sum(scores) / len(scores)
    print(f"{student}: average {average:.2f}")

#Filter a dictionary based on a condition
ages = {"Ana": 17, "Luis": 22, "Marta": 15, "Pedro": 30}
adults = {name: age for name, age in ages.items() if age >= 18}
print(adults) 

#6_Object-Oriented Programming 
#Person class
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def greet(self):
        print(f"Hi, I'm {self.name} and I'm {self.age} years old")
p = Person("Ana", 25)
p.greet()

#Simple bank account
class BankAccount:
    def __init__(self, initial_balance=0):
        self.balance = initial_balance
    def deposit(self, amount):
        self.balance += amount
    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds")
        else:
            self.balance -= amount
    def check_balance(self):
        return self.balance
account = BankAccount(100)
account.deposit(50)
account.withdraw(30)
print(account.check_balance()) 

#Rectangle class
class Rectangle:
    def __init__(self, base, height):
        self.base = base
        self.height = height
    def area(self):
        return self.base * self.height
    def perimeter(self):
        return 2 * (self.base + self.height)
r = Rectangle(4, 5)
print(r.area(), r.perimeter())

#Inheritance and method overriding 
class Animal:
    def make_sound(self):
        print("Generic animal sound")
class Dog(Animal):
    def make_sound(self):
        print("Woof")
class Cat(Animal):
    def make_sound(self):
        print("Meow")
for animal in [Dog(), Cat()]:
    animal.make_sound()

#7_Exception Handling
#Division protected against zero
try:
    a = float(input("Enter the first number: "))
    b = float(input("Enter the second number: "))
    result = a / b
    print(f"Result: {result}")
except ZeroDivisionError:
    print("Error: cannot divide by zero")

#Validate numeric input
try:
    number = int(input("Enter a number: "))
    print(f"The number entered is {number}")
except ValueError:
    print("That's not a valid number")

#Handle a missing file
try:
    with open("missing_file.txt", "r") as file:
        content = file.read()
except FileNotFoundError:
    print("The file doesn't exist")

#Custom validation for age
def validate_age(age):
    if not isinstance(age, (int, float)) or age < 0 or age >= 120:
        raise ValueError("Age must be a number between 0 and 119")
    return age
try:
    validate_age(-5)
except ValueError as error:
    print(f"Error: {error}")


#Capstone Project 
class InsufficientQuantityError(Exception):
    pass
class ProductNotFoundError(Exception):
    pass
class Product:
    def __init__(self, name, price, quantity, category="General"):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.category = category
    def __str__(self):
        return f"{self.name} | ${self.price} | {self.quantity} units | {self.category}"
class Inventory:
    def __init__(self, file_path="inventory.txt"):
        self.file_path = file_path
        self.products = []
        self.load()
    def add_product(self, product):
        self.products.append(product)
        self.save()
    def remove_product(self, name):
        product = self.find_product(name)
        self.products.remove(product)
        self.save()
    def find_product(self, name):
        for product in self.products:
            if product.name.lower() == name.lower():
                return product
            raise ProductNotFoundError(f"Product '{name}' was not found")
    def update_quantity(self,name,new_quantity):
        product = self.find_product(name)
        if new_quantity < 0:
            raise InsufficientQuantityError("Quantity cannot be negative")
        product.quantity = new_quantity
        self.save()
    def summary_by_category(self):
        summary = {}
        for product in self.products:
            summary[product.category] = summary.get(product.category, 0) + product.quantity
        return summary
    def save(self):
        with open(self.file_path, "w") as file:
            for p in self.products:
                file.write(f"{p.name},{p.price},{p.quantity},{p.category}\n")
    def load(self):
        try:
            with open(self.file_path, "r") as file:
                for line in file:
                    name, price, quantity, category = line.strip().split(",")
                    self.products.append(Product(name, float(price), int(quantity), category))
        except FileNotFoundError:
            self.products = []

    def menu():
        inventory = Inventory()
        while True:
            print("\n1. Add product\n2. Remove product\n3. Update quantity")
            print("4. View inventory\n5. Summary by category\n6. Exit")
            choice = input("Choose an option: ")
            try:
                if choice == "1":
                    name = input("Name: ")
                    price = float(input("Price: "))
                    quantity = int(input("Quantity: "))
                    category = input("Category: ")
                    inventory.add_product(Product(name, price, quantity, category))
                elif choice == "2":
                    name = input("Name of the product to remove: ")
                    inventory.remove_product(name)
                elif choice == "3":
                    name = input("Product name: ")
                    quantity = int(input("New quantity: "))
                    inventory.update_quantity(name, quantity)
                elif choice == "4":
                    for p in inventory.products:
                        print(p)
                elif choice == "5":
                    print(inventory.summary_by_category())
                elif choice == "6":
                    break
                else:
                    print("Invalid option")
            except (ProductNotFoundError, InsufficientQuantityError, ValueError) as error:
                print(f"Error: {error}")
    if __name__ == "__main__":
        menu()
















