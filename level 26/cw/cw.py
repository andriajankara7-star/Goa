for i in range(0, 26):
    if i % 2 == 0:
        print(i)
#პირობითი განცხადებით თუ if-ში რაც არის ის არასწორია მაშინ elif-ით გამოიტანს
num = int(input("enter the number 999 or 998:"))
if num == 999:
    print("the number is 999")
elif num == 998:
    print("the number is 998")


password = "i am a burger"
user_input =  ""
while user_input == password:
    print("Incorrect Password")
user_input = input("enter your password:")
if user_input == password:
    print("correct password")
else:
    print("Incorrect password")
    user_input = input("wrong password try again:")