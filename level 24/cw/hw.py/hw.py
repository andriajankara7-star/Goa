numb = int(input("enter a number:"))

if numb % 2 == 0:
    print("even")
else:
    print("odd")

num = int(input("enter a number:"))
if num > 0:
    print("true")
else: 
    print("false")


age = int(input("enter your age: "))

if age >= 18:
    print("you can speak")
else:
    print("your small you can speak after you grow up")


score = int(input("enter your score (0-100): "))

if score >= 50:
    print("Passed")
else:
    print("Failed")

password = "1234"
user_input = input("enter your password:")

if user_input == password:
    print("Correct password")
else:
    print("Incorrect password")