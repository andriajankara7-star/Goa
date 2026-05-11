age = int(input("enter your age:"))
if age >= 18:
    print("you are an adult")
else:
    print("you are not an adult")

word = input("enter a word:")

for i in word:
    print(i)

for i in range(1, 16):
    if i % 3 == 0:
        print(i)