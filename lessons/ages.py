"""Example memory diagram program"""

age: int = int(input("How old are you? "))
year: int = int(input("What year is it? "))
age_in_2021: int = 2041 - year + age
print("In year 2041, you'll be " + str(age_in_2021))

age = age + 1
year = year + 1
print("In " + str(year) + ", you'll be " + str(age))
