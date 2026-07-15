# .upper() სიტყვას აკეთებს ყველას დიდ ასოდ. .lower() აკეთებს სიტყვას ყველას პატარა ასოდ. .capitalize() აკეთებს პირველ ასოს დიდს და დანარჩენს პატარას. .find() პოულობს მაგ ასოს ან ასოებს სიტყვაში და ინდექს გეტყვის სადაც არის თუ .find() ში არგუმენტი არ წერია ერორს გამოიტანს და თუ ვერ იპოვის გამოიტანს -1-თს მაგ:
print("andro".upper())
print("andro".lower())
print("andro".capitalize())
print("androoooio".find("io"))

# len() - გვეუბნება ლისტში რამდენი ინდექსი არის და ცვლადში რამდენი ასოა
#  append() - ლისტში სულ ბოლო ინდექსად ამატებს შენ რასაც ჩაწერ 
# insert() - ლისტში ამატებს შენ რა ინდექსაც მიუთითებ რასაც ჩაწერ
# pop() - შლის ინდქსს რასაც შენ აირჩებ. მაგ:
movies = ["titanic", "avatar" , "avengers"]
print(len(movies))
movie = "stranger things"
print(len(movie))
movies.append("spider man")
movies.insert(1 , "ar vici")
movies.pop(1)
print(movies)
# split ცვლადში ყველა სიტყვას ინდექსებად გადააქცევს მაგ:
andro = "my name is andro"
print(andro.split())
# სტრინგი არის სიმბოლოების მიმდევრობა და უცვლადი ტიპია.
# ლისტი არის ელემენტების კოლექცია და ცვლადი ტიპია