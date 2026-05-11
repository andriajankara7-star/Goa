price = 190
your_money = int(input("enter your money:"))
if price <= your_money:
    print("you can afford it")
elif price > your_money:
    print("you cant afford it")

number = int(input("enter a number:"))

if number % 2 == 0:
    print("Even")
else:
    print("Odd")