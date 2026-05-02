
#Day 3: If-Else Practice 
#1. Basic Decision
num  = int(input("Enter a number:"))
if num > 0:
      print("Number is positive")
elif num < 0:
      print("Number is negative:")
else:
      print("Number is zero")      
      
#2. Even/Odd Filter
Num = int(input("Enter a number:"))      
if Num % 2 == 0:
      print("Number is even")
elif Num > 100:
      print("Number is large")
else:
      print("Number is odd")            
      
#Salary Tax Bracket      

salary = float(input("Enter your salary: "))
tax = 0

if salary < 300000:
    tax = 0

elif salary <= 700000:
    tax = salary * 0.10

elif salary <= 1200000:
    tax = salary * 0.20

else:
    tax = salary * 0.30

print("Your tax is:", tax)

#4. Data Validation (Critical Skill)
Age = int(input("Enter your Age:"))
if Age < 0:
     print("Invalid data!")
elif Age < 18:
     print("Minor")
else:
     print("Adult")        

#5. Login System Simulation
correct_username = "Anamika" 
correct_password = "anamika@123"
username = input("Enter a username:")
password = input("Enter a password:")
if username == correct_username and password == correct_password:
     print("Login success")
elif username !=  correct_username:
     print("Invalid username")
else:
     print("Invalid Password")     

#6. Data Quality Check
str = input("Enter a string:")
if len(str) == 0:
     print("Missing data")
elif len(str) < 3:
     print("Invalid data")   
else:
     print("Valid data")

#7 Data quality check
price = float(input("Enter price: "))
user_type = input("Enter user type (new/premium/vip): ").lower().strip()

discount = 0

if user_type == "premium":
    discount = price * 0.20
elif user_type == "new":
    discount = price * 0.10
elif user_type == "vip":
    discount = price * 0.30
elif user_type == "":
    print("Invalid input: empty user type")
    exit()
else:
    print("Invalid user type")
    exit()

final_price = price - discount

print("\n--- BILL ---")
print("Original Price:", price)
print("Discount:", discount)
print("Final Price:", final_price)

#8. Temperature Alert System
Temperature = float(input("Enter tempertature((in degree celsius)):"))
if Temperature < 0:
     print("Freezing alert!")
elif 0 >= Temperature <=30: 
     print("Normal")
else:
     ("high temperature alert") 


# Data Pipeline Status Simulation
status = input("Enter pipeline status (success/failed/running): ").strip().lower()

if status == "success":
    print(" Data loaded successfully. Proceeding to next task.")
elif status == "failed":
    print(" Error detected! Check logs and trigger alert.")
elif status == "running":
    print(" Processing in progress... please wait.")
else:
    print(" Unknown Status: System status unrecognized.")

#10. Nested Conditions (Important)
marks = float(input("Enter your marks:"))
attendance = float(input("Enter your attendance(in%):"))
if marks >= 40:
     if attendance >= 75:
          print("Pass")
     else:
          print("failed due to low attendance")
else:
     print("failed due to marks")              

#11. Multiple Conditions (AND / OR)
Age = int(input("Enter your age:"))
has_id =input("enter(True/False):")
if Age >= 18 and has_id == "True":
     print("Allowed Entry")
else:
     print("Denied")

#12. Fraud Detection 
amount = float(input("Enter transaction amount: "))
location = input("Enter location: ")
if amount > 50000 and location == "foreign":
    print("Large foreign transaction detected.")
else:
     print("Normal")


# Mini Project 
#Build a User Eligibility Checker:     
# 1. Collect inputs
age = int(input("Enter age: "))
income = float(input("Enter annual income: "))
credit_score = int(input("Enter credit score: "))

if age < 0 or income < 0 or credit_score < 0:
    result = "Invalid Data"

elif age < 18:
    result = "Rejected (Age < 18)"

elif income < 20000:
    result = "Rejected (Low Income)"

elif credit_score < 600:
    result = "Risky (Low Credit Score)"

else:
    result = "Approved"

print("\n--- Eligibility Report ---")
print("Age:", age)
print("Income:", income)
print("Credit Score:", credit_score)
print("Final Status:", result)




