# Print numbers from 1 to 20 using for loop
# Then do same using while loopprint("For Loop:")
for i in range(1, 21):
    print(i, end=" ")

print("\n") 
# Using a while loop
print("While Loop:")
i = 1
while i <= 20:
    print(i, end=" ")
    i += 1
print("\n")     

#2. Sum of Numbers   
# # Input: n
# Find sum of numbers from 1 to n using loop 
n = int(input("Enter number:"))
sum= 0
for i in range(1,n):
    sum = sum+i

print("The sum of numbers",sum)

#3. Count Even & Odd
# Input: list of numbers
# Count how many are even and how many are odd
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

even_count = 0
odd_count = 0

for num in numbers:
    if num % 2 == 0:
        even_count += 1
    else:
        odd_count += 1

print(f"Even numbers: {even_count}")
print(f"Odd numbers: {odd_count}")

#4. Data Cleaning Loop
data = ["10", "", "apple", "25", " ", "42", "3.14"]
valid_numbers = []

for item in data:
    # strip() handles empty strings and whitespace
    if item.strip() and item.strip().isdigit():
        valid_numbers.append(int(item))

print(valid_numbers)

#5. Max Value Finder
list = [23,67,46,9,34,24]
print(max(list))

#6. Frequency Counter (Important)
data = [1, 2, 2, 3, 3, 3, 4]
frequency = {}

for item in data:
    if item in frequency:
        frequency[item] += 1
    else:
        frequency[item] = 1

print(frequency)

#7. Break Statement
# Loop from 1–100
# Stop when number divisible by 17 is found
for i in range(1,101):
    if i% 17 == 0:
         print(i)
         break
    

#8. Continue Statement3
for i in range(1,21):
    if i % 3 == 0:
        continue
    print(i)
         
#. Nested Loop (Data Grid)
for row in range(1, 6):          
    for col in range(1, 6):      
        print(f"({row},{col})", end=" ")
    print()                      

#Password Attempts (While Loop)
correct_password = "secret_password"
attempts = 3

while attempts > 0:
    guess = input(f"Enter password ({attempts} attempts left): ")
    
    if guess == correct_password:
        print("Access Granted: Success!")
        break
    else:
        attempts -= 1
        if attempts > 0:
            print("Incorrect password. Try again.")
        else:
            print("Access Denied: Account blocked.")


running_total = 0
while True:
    val = int(input("Enter a number(or -1 to stop):")) 
    if val == -1:
        break

running_total += val  
print(f"Current Total: {running_total}")  

print(f"Final Total: {running_total}")  

#12. List Transformation
data = [1, 2, 3, 4, 5]
new_list = []

for i in data:
    square = i**2         
    new_list.append(square) 
print(new_list)

#Build a Sales Analyzer
sales = [1000, 2000, 1500, 3000, 500, 700]

total_sales = 0
high_sales_count = 0
max_sale = 0


for sale in sales:
    total_sales += sale
    
    if sale > 1500:
        high_sales_count += 1
    
    if sale > max_sale:
        max_sale = sale

average_sale = total_sales / len(sales)

print(f"Total Sales: {total_sales}")
print(f"Average Sale: {average_sale:.2f}")
print(f"Sales > 1500: {high_sales_count}")
print(f"Maximum Sale: {max_sale}")
