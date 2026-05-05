#1. Basic Function
# Create a function that prints "Hello Data Engineer"
# Call it 3 times
def greet_data_engineer():
    print("Hello Data Engineer")
for _ in range(3):
    greet_data_engineer()

#2. Function with Parameters
# Create function:
# takes name as input
# prints: "Hello <name>"
def greet_person(name):
    print(f"Hello {name}")
greet_person("Alice")

#. Return Value
# Function:
# takes two numbers
# returns their sum
def sum(a,b):
    return a+b
result = sum(3,2)
print(f"The sum is:{result}")

#Even/Odd Checker
# Function:
# takes number
# returns "Even" or "Odd"
def checker(num):
    if num % 2 == 0:
        return "even"
    else:
        return "odd"
result = checker(9) 
print(result)   

#. Max of Three Numbers
# Function:
# takes 3 numbers
# returns largest
def largest(a,b,c):
    if a > b and a >c:
        return a
    elif b > a and b > c:
        return b
    else:
        return c
result = largest(45,67,9)
print(result)    

#Cleaning Function (Important)
# Function:
# takes list:
def clean_integers(data):
    return [int(i) for i in data if i.isdigit()]

data = ["10", "", "abc", "30"]
print(clean_integers(data))

#. Salary Tax Function
# Function:
# takes salary
# returns tax (use slab logic)
def calculate_tax(salary):
    tax = 0

    if salary > 1000000:
        tax += (salary - 1000000) * 0.30
        salary = 1000000

    if salary > 500000:
        tax += (salary - 500000) * 0.20
        salary = 500000

    if salary > 250000:
        tax += (salary - 250000) * 0.05
        salary = 250000

    return tax
print(calculate_tax(1200000))

#8. List Sum Function
# Function:
# takes list
# returns sum using loop (no sum())
def total(list):
    add = 0
    for i in list:
        add += i
    return add 
list =[30,20,45,34] 
print(total(list))  


#9. Count Elements
# Function:
# takes list + target value
# returns how many times it appears
def count_occurence(data,target):
    count = 0
    for item in data:
        if item == target:
            count+= 1
    return count
    
logs = ["INFO","ERROR","INFO","WRONG","INFO"]
print(count_occurence(logs,"INFO")) 

#Login Function
# Function:
# takes username + password
# returns:
# "Success" / "Invalid"

def login(username,password):
    correct_user = "admin"
    correct_pass = "secret123"
    if username == correct_user and password == correct_pass:
        return "sucess"
    else:
        return "invalid"
print(login("admin","secret123"))
print(login("admin","secert@123"))

# Mini Project (Mandatory)
#Build a User Data Processor

users = [
    {"name": "A", "age": 25},
    {"name": "B", "age": -5},
    {"name": "C", "age": 30}
]
def process_user_data(user_list):
    clean_users = []
    
    for user in user_list:
       
        if user["age"] >= 0:
            clean_users.append(user)
            
    count = len(clean_users)
    return clean_users, count
cleaned_data, total_valid = process_user_data(users)

print(f"Cleaned List: {cleaned_data}")
print(f"Valid User Count: {total_valid}")
