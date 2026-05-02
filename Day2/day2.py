#Variable Basics
your_name = "John Doe"
your_age = 30
your_height = 175.5
is_student = True
print("Name:", your_name)
print("Age:", your_age)
print("Height (cm):", your_height)
print("Is Student:", is_student)

#Type Checking
#Create 5 variables with different data types.
#Print their types using type()
var1 = "Hello, World!"
var2 = 42
var3 = 3.14
var4 = True
var5 = [1, 2, 3]
print("Type of var1:", type(var1))
print("Type of var2:", type(var2))
print("Type of var3:", type(var3))
print("Type of var4:", type(var4))
print("Type of var5:", type(var5))

# Type Conversion
num_str = "25"
num_int = int(num_str)
num_float = float(num_str)
print("String:", num_str+str(10))
print("Integer:", num_int+10)
print("Float:", num_float+10.0)

#Input + Data Type Handling
#Take user input:
age = int(input("Enter your age: "))
salary = float(int(input("Enter your monthly salary: ")))
#Convert to correct types and print:
print("After 5 years, your age will be", age + 5)
print("Your monthly salary is", salary)

#String Operations
data_engineering = "Data Engineering"
print("First character:", data_engineering[0])
print("Last character:", data_engineering[-1])
print("Reverse string:", data_engineering[::-1])
print("Length of string:", len(data_engineering))

#6. Numeric Operations
num1 = 10
num2 = 3
print("Addition:", num1 + num2)
print("Subtraction:", num1 - num2)
print("Multiplication:", num1 * num2)
print("Division:", num1 / num2)
print("Floor Division:", num1 // num2)
print("Modulus:", num1 % num2)
print("Exponentiation:", num1 ** num2)
print("Square Root of num1:", num1 ** 0.5)
print("Square Root of num2:", num2 ** 0.5)

#7. Boolean Logic
#Create two boolean variables
bool1 = True
bool2 = False
#Print results of:
print("AND:", bool1 and bool2)
print("OR:", bool1 or bool2)
print("NOT bool1:", not bool1)
print("NOT bool2:", not bool2)

#list
my_list = [1, "Hello", 3.14, True]
print("first element",my_list[0])
print("last element",my_list[-1])
print("length of list",len(my_list))
my_list.append("New Element")
print("Updated list",my_list)
my_list.remove("New Element")
print(my_list)      

#9. Tuple vs List
list = [1,3.2,"hello",False]
tuple = (2,4.5,"go",True)
list.append(4)
print(list)
print(tuple)

#Mini challenge
#Create variables:
user_id = int(input("Enter user id:"))
user_name = input("Enter user name:")
is_active = input("Is the user active? (True/False): ").lower() == "true"
balance = float(input("Enter account balance: "))

# Displaying the captured data
print(f"\nProfile for {user_name}:")
print(f"ID: {user_id} | Active: {is_active} | Balance: ${balance:.2f}")
