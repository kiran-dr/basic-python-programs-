# 16. Python program to find sum of first n natural numbers
n = int(input("Enter input: "))
sum_n = n * (n + 1) // 2
print("Sum =", sum_n)

# 17. Python program for arithmetic operations
a = 10
b = 20
print("Addition =", a + b)
print("Subtraction =", a - b)
print("Multiplication =", a * b)
print("Modulo =", a % b)

# 18. Python program to demonstrate logical operators
a = 10
b = 12
print(a > 0 and b > 15)
print(a > 15 or b > 5)
print(not(a == 10))

# 19. Python program to check positive, negative, or zero
a = int(input("Enter the number: "))
if a > 0:
    print("Positive")
elif a < 0:
    print("Negative")
else:
    print("Zero")

# 20. Python program to check even or odd
a = int(input("Enter the number: "))
if a % 2 == 0:
    print("Number is even")
else:
    print("Number is odd")

# 21. Python program to check divisibility by 5 and 11
a = int(input("Enter the number: "))
if a % 5 == 0 and a % 11 == 0:
    print("The number is divisible by 5 and 11")
else:
    print("The number is not divisible by 5 and 11")

# 22. Python program to check age group
age = int(input("Enter your age: "))
if age <= 10:
    print("Child")
elif 10 < age <= 21:
    print("Teenage")
else:
    print("Adult")

# 23. Python program to check grade using marks
m = int(input("Enter your marks: "))
if m >= 90:
    print("A-grade \nExcellent!")
elif 80 <= m < 90:
    print("B-grade \nGood!")
elif 70 <= m < 80:
    print("C-grade \nAverage!")
elif 60 <= m < 70:
    print("D-grade \nPoor!")
else:
    print("F-grade \nFail!")

# 24. Python program to check day based on user input between 1 to 7
day = int(input("Enter a number between 1 to 7: "))
if day == 1:
    print("Monday")
elif day == 2:
    print("Tuesday")
elif day == 3:
    print("Wednesday")
elif day == 4:
    print("Thursday")
elif day == 5:
    print("Friday")
elif day == 6:
    print("Saturday")
elif day == 7:
    print("Sunday")
else:
    print("Invalid Input")

# 25. Python program to check username and password credentials
u_name = input("Enter Username: ")
password = input("Enter Password: ")
if u_name == "kiran-dr" and password == "12345":
    print("Login Successful")
else:
    print("Invalid Credentials")

# 26. Python program to develop a calculator
a = int(input("Enter number1: "))
b = int(input("Enter number2: "))
choice = int(input("Enter your choice: \n1. Addition \n2. Subtraction \n3. Multiplication \n4. Division\n"))
if choice == 1:
    print(f"{a} + {b} =", a + b)
elif choice == 2:
    print(f"{a} - {b} =", a - b)
elif choice == 3:
    print(f"{a} * {b} =", a * b)
elif choice == 4:
    if b != 0:
        print(f"{a} / {b} =", a / b)
    else:
        print("Division by zero is not allowed")
else:
    print("Invalid choice")

# 27. Python program to print number of days in month
month = int(input("Enter a month number: "))
if month in (1, 3, 5, 7, 8, 10, 12):
    print("31 days")
elif month in (4, 6, 9, 11):
    print("30 days")
elif month == 2:
    print("28 days if not a leap year \n29 days if it’s a leap year")
else:
    print("Invalid month")

# 28. Python program to check body temperature
t = int(input("Enter your body temperature: "))
if t > 36:
    print("Fever")
elif t == 36:
    print("Normal")
else:
    print("Cold")

# 29. Python program to print sum of cubes from m to n
m = int(input("m: "))
n = int(input("n: "))
sum = 0
if m > n:
    print(0)
else:
    for i in range(m, n + 1):
        sum = sum + i ** 3
    print(f"Sum of cubes from {m} to {n} =", sum)

# 30. Python program to check voting eligibility
age = int(input("Enter your age: "))
if age >= 18:
    print("You are eligible to vote")
else:
    print("You are not eligible to vote")