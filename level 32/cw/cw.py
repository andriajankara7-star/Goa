num = int(input("enter a number:"))
if num < 0:
    print("უარყოფითი")
else:
    print("დადებითი")

sales = [45, 50, 62, 40, 55, 90, 105]
print(sales[0])
print(sales[2])
print(sales[-1])
sales[3] = 48
print(sales)

ratings = [8.5, 7.2, 9.0, 6.8, 9.5]
print(ratings[1])
print(ratings[3])
print(ratings[-1])
ratings[2] = 9.3
print(ratings)