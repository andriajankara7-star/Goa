#if else და elif გვეხმარება რომ დავწეროთ მაგალითები და if-ს გამოვიყენებთ თუ მაგალითი მეტია 
# else გამოვიყენებთ თუ მაგალითი ნაკლებია
# elif-ს გამოვიყენებთ თუ ტოლია

num = int(input("enter a number:"))
if num > 0:
    print("num is more than 0")
else:
    print("num is less than 0")

password = "goabest123"
password2 = input("enter your password:")
if password == password2:
    print("correct password")
else:
    print("incorrect password")

abc = int(input("enter a number"))
defg = int(input("enter a number"))
print(abc + defg)