# Name: Vanathi Selvan
# Date: 6/19/17

# proj01: A Simple Program
# This program asks the user for his/her name and age.
# Then, it prints a sentence that says when the user will turn 100.

# If you complete extensions, describe your extensions here!

print "Hello World!"

name = raw_input("Enter your name: ")

print name

age = raw_input("Enter your age: ")
age_int = int(age)

birthday = raw_input("Has your birthday already been completed?: ")
if birthday == "yes":
    age_int_hundred = (100 - age_int)
    print "That's amazing"
    print name, "You will be 100 years old in ", age_int_hundred, "years."
    print age
    print age_int_hundred
else:
    age_int_hundred = (101 - age_int)
    print "I hope you are excited for your birthday soon!"
    print name, "You will be 100 years old in ", age_int_hundred, "years."

movie = raw_input ("What type of movie are you interested in or allowed to watch?: ")
if movie == "G":
    print "Select Movies in Genre G"


if movie == "PG":
    print "Select Movies in Genre PG"


if movie  == "PG-13":
    if age_int >= 13:
        print "allow"
    if age_int <= 13:
        print "Denied"
        permission = raw_input ("What type of movie are you interested in or allowed to watch?: ")
        print "Go back to Main Menu or use Parents/Guardians Touch ID"

if movie == "R":
    print age_int
    if age_int > 17:
        print "Select Movies in Genre R"
    if age_int <= 17:
        print "Denied"









year = raw_input("Enter your year: ")
year_int = age_int

print name, "You will be 100 years old in ", age_int, " years."












