password = "32942"
user_input = input("Enter your password: ")

while password != user_input:
    user_input = input("Enter your password: ")
    print("Try again")
print("Correct password")

age = int(input('Enter your age: '))
if 18 < age:
    print("regular price")
else:
    print("discount")
    