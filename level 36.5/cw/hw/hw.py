# ლოგიკური ოპერატორები არის if else elif
# while loop იყენებს ლოგიკურ ოპერატორებს for loop-ი რეინჯს ვაილ ლოოპით შენ არ იცი რამდენჯერ გამეორდება ფორ ლოოპით კი
name = str(input("enter a name:"))
name1 = "andro"
if name == name1:
    print("correct name")
else:
    print("incorrect name")
# def არის ფუნქცია მას შეგვიძლია დავუწეროთ გვერდით რამე მაგ: greet(): მერე ორ წერტილმა ინდენტაცია რომ შექმნა დაბლა მანდ ჩავალთ და პრინტ რამეს დავწერთ მაგ:
def greet():
    print("hello")
greet()
def greet_age_name():
    print("hello")
    print("my name is andro")
    print("i am 10 years old")
greet_age_name()