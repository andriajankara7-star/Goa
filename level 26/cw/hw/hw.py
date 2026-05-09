score = (int(input("enter your score:")))
if score > 89:
    print("A")
elif score > 79:
    print("B")
elif score > 69:
    print("C")
elif score > 59:
    print("D")
elif score < 60:
    print("F")

num = (int(input("enter a number:")))
if num > -1:
    print("positive")
else:
    print("negative")
num1 = (int(input("enter a number:")))
num2 = (int(input("enter a number:")))
if num1 > num2:
    print("the first number is greater that the second one")
else:
    print("the second number is greater that the first one")
num3 = (int(input("enter a number:")))
if num3 % 2 is 1:
    print("odd")
else:
    print("even")
num4 = (int(input("enter a temperature number:")))
if num4 < 0:
    print("cold")
elif num4 < 30:
    print("normal")
elif num4 > 30:
    print("hot")