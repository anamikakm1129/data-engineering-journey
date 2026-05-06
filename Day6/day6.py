#1. Clean & Sum Data
# Task:
# - clean invalid values
# - convert to int
# - return total sum using function
def clean_and_sum(data_list):
    total = 0
    for item in data_list:
        try:
            # If this fails, it jumps to 'except' instead of crashing
            total += int(item)
        except ValueError:
            # Skip the invalid data and keep looping
            continue
    return total

data = ["10", "20", "", "abc", "30"]
result = clean_and_sum(data)
print(f"Total Sum: {result}") 

#data = ["10", "20", "", "abc", "30"]


#2. Count Valid Users
users = [
    {"name": "A", "age": 25},
    {"name": "B", "age": -2},
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

#3. Even Numbers Extractor
# Task:
# - create function
# - return list of even numbers
def even(numbers):
    list = []
    for num in numbers:
        if num % 2 == 0:
            list.append(num)
    return list        
numbers = [1,2,3,4,5,6,7,8]
print(even(numbers))

# Max Sale Finder
# Task:
# - find max without max()
# - use loop
def maximum(sales):
    max = sales[0]
    for i in sales:
        if i > max:
            max == i
    return max 

sales = [1000, 2000, 1500, 3000, 500]
print(max(sales))   

#5. Password Validator
# Task:
# Function takes password
# Conditions:
# - length < 6 → invalid
# - must contain digit
# - return "Valid" / "Invalid"
def pass_checker(password):
    password = str(password)
    
    if len(password) >= 6 and any(ch.isdigit() for ch in password):
        return "Valid"
    return "Invalid"
print(pass_checker("1235566"))
print(pass_checker("1566"))

#6. Transaction Filter
transactions = [100, -50, 300, None, 500]

# Task:
# - ignore None
# - ignore negative
# - return cleaned list
def clean_transactions(transactions):
    cleaned = []
    for t in transactions:
        if t is not None and t >= 0:
            cleaned.append(t)
    return cleaned
print(clean_transactions(transactions))

#7. Frequency Counter

# Task:
# - count frequency using loop
# - return dictionary
def freq(data):
    frequency ={}
    for i in data:
        if freq in data:
            frequency[i] += 1
        else:
            frequency[i] = 1
    return frequency
data = [1,2,2,3,3,3,4]

print(freq(data))       

#8. Prime Numbers List
# Task:
# Function takes n
# return list of prime numbers from 1 to n

def prime_list(n):
    primes = []
    
    for num in range(2, n + 1):
        is_prime = True
        
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
        
        if is_prime:
            primes.append(num)
    
    return primes


print(prime_list(20))

#9. Salary Processor
# Task:
# - calculate tax for each
# - return new list of taxes
def calculate_tax(salaries):
    return [s * 0.10 for s in salaries]


salaries = [20000, 50000, 100000]  
print(calculate_tax(salaries))

#. Mini Project
def process_orders(orders):
    result = []
    
    for order in orders:
        if order["status"] == "paid":
            result.append("Process")
        
        elif order["status"] == "pending" and order["amount"] > 10000:
            result.append("Hold")
        
        else:
            result.append("Ignore")  # fallback for undefined cases
    
    return result


orders = [
    {"amount": 5000, "status": "paid"},
    {"amount": 15000, "status": "pending"},
    {"amount": 20000, "status": "paid"}
]

print(process_orders(orders))