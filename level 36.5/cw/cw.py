age = int(input("what is your age:"))
yes_or_no = input("do you have the doctors premmision (yes or no):")
yes = "yes"
no = "no"
if age >= 18 and yes_or_no == yes:
    print("you can train")
elif age < 18 and yes_or_no == no:
    print("you are under 18 and dont have doctors premmision")
elif age >= 18 and yes_or_no == no:
    print("you dont have doctors premmision")
elif age < 18 and yes_or_no == yes:
    print("your under 18")
for i in range(11):
    print(i * i)
for i in range(11):
    print(i ** 2)
for i in range(1 , 11):
    a = i ** 2
    if a > 30:
        print(f"რიცხვი {i}-ის კვადრატია {a} და ის მეტია 30ზე")
password = 8520
password1 = int(input("enter the password (with numbers):"))
while password1 != password:
    print("incorrect")
    password1 = int(input("enter the password (with numbers):"))
print("correct password")
        
