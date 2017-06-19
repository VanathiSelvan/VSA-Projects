# Name:
# Date:



name = raw_input("Enter your name: ")
age = int(raw_input("Enter your age: "))
birthday = raw_input("Has your birthday happened this year? Enter Y or N: ")

if birthday == "Y":
    year_100 = str((100 - age) + 2017)

else:
    year_100 = str((100 - age) + 2016)

while age < 101:
    print
    year = year + 1


print name, " will turn 100 in the year ", year_100, "."
