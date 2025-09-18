# 1. Python program to print your name
n = "v.abhishek"
print(n)

# 2. Python program to get the input from the user and print it
name = input("Enter your name: ")
print(name)

# 3. Python program to get input from user and print multiple numbers
num1 = input("Enter your first number: ")
num2 = input("Enter your second number: ")
print("First number:", num1)
print("Second number:", num2)

# 4. Python program to add two numbers
num3 = int(input("Enter your third number: "))
num4 = int(input("Enter your fourth number: "))
sum_ = num3 + num4
print("Sum of two values:", sum_)

# 5. Python program to generate full name
a = input("Enter the first name: ")
b = input("Enter the second name: ")
c = a + b
print("Your full name:", c)

# 6. Python program to swap two numbers without third variable
a = 10
b = 20
a = a + b
b = a - b
a = a - b
print("After swapping a:", a)
print("After swapping b:", b)

# 7. Python program to swap two numbers using third variable
a = 10
b = 20
temp = a
a = b
b = temp
print("After swapping a:", a)
print("After swapping b:", b)

# 8. Python program to print primitive data types
a = 10
b = 2.13
c = True
print("Integer is:", a)
print("Float is:", b)
print("Boolean is:", c)

# 9. Python program to print non-primitive data types
a = (10, 20, 30)
b = [10, 10, 20, 30]
c = {10, 20, 20, 30}
dict_1 = {"one": 1, "two": 2}
print(a)
print(b)
print(c)
print(dict_1)

# 10. Python program to find square of a number
a = int(input("Enter a number: "))
square = a * a
print("Square of a number:", square)

# 11. Python program to find average of three numbers
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
c = float(input("Enter third number: "))
avg = (a + b + c) / 3
print("Average is:", avg)

# 12. Python program to multiply a number by 10
a = int(input("Enter a number: "))
b = a * 10
print("After multiplying with 10:", b)

# 13. Python program to convert minutes into seconds
a = int(input("Enter minutes: "))
sec = a * 60
print("Seconds =", sec)

# 14. Python program to multiply floating point numbers
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
product = a * b
print("Product =", product)

# 15. Python program to find largest of three numbers
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
c = float(input("Enter third number: "))
largest_number = max(a, b, c)
print("Largest number is:", largest_number)

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
