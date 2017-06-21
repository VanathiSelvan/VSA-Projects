
# num = raw_input("What number do you want to find divisors for: ")

def divisors (num):
   myList = []
   c = int(num)
   for c in range (1, num + 1):
       a = int(num) % c
       if a == 0:
           myList.append(c)
       c = c - 1
   return myList
print divisors(8)
a = divisors
def prime(num):
    myList = divisors(num)
    length = len(myList)
    if length == 2:
        return True
    else:
        return False

import random
lst1 = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
lst2= [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
list = [1, 2 ,1 ,1 ,1 ,3 ,2 ,1 ,2 ,1 ,2]
nextnum = 0
for number in list:
    list[nextnum] = random.randint(1,99)
    nextnum = nextnum + 1
print list
def intersection(lst1, lst2):
    myList = []
    for numbers in lst1:
        if numbers in lst2:
            myList.append(numbers)
    print myList
    return myList


def find_ab(side1, side2, side3):
    if side1 > side2 and side1 > side3:
        return [side2,side3]
    elif side2 > side1 and side2 > side3:
        return [side1,side3]
    elif side3 > side1 and side3 > side2:
        return [side1,side2]

def find_c(side1, side2, side3):
    if side1 > side2 and side1 > side3:
        return side1
    elif side2 > side1 and side2 > side3:
        return side2
    elif side3 > side1 and side3 > side2:
        return side3
def square(side1):
    return side1 * side1
def pythagorean(a,b,c):
    if square(a) + square(b) == square(c):
        return True
    else:
        return False
def is_right(side1, side2, side3):
    small = find_ab(side1,side2,side3)
    a = small[0]
    b = small[1]
    c = find_c(side1,side2,side3)
    p = pythagorean(a,b,c)
    return p






















































# TESTS
# Feel free to add your own tests as needed!

print ("Divisors Tests")
# Test 1
if divisors(1) == [1]:
    print("Test 1: PASS")
else:
    print("Test 1: FAIL")

# Test 2
if divisors(8) == [1,2,4,8]:
    print("Test 2: PASS")
else:
    print("Test 2: FAIL")

# Test 3
if divisors(9) == [1,3,9]:
    print("Test 3: PASS\n")
else:
    print("Test 3: FAIL\n")

print("Prime Tests")
# Test 4
if prime(9):
    print("Test 4: FAIL")
else:
    print("Test 4: PASS")

# Test 5
if prime(7):
    print("Test 5: PASS\n")
else:
    print("Test 5: FAIL\n")

L1 = []
L2 = [3, 4]
L3 = [3, "a"]
L4 = [5, "b", 10, 7, "a"]
L5 = [5, 7, 11]

print("Intersection Tests")
# Test 6
if intersection(L1, L2) == []:
    print("Test 6: PASS")
else:
    print("Test 6: FAIL")

# Test 7
if intersection(L2, L3) == [3]:
    print("Test 7: PASS")
else:
    print("Test 7: FAIL")

# Test 8
if intersection(L2, L4) == []:
    print("Test 8: PASS")
else:
    print("Test 8: FAIL")

# Test 9
if intersection(L3, L4) == ["a"]:
    print("Test 9: PASS")
else:
    print("Test 9: FAIL")

# Test 10
if intersection(L4, L5) == [5, 7]:
    print("Test 10: PASS\n")
else:
    print("Test 10: FAIL\n")

print("Is_Right Tests")
# Test 11
if is_right(5, 3, 4):
    print("Test 11: PASS")
else:
    print("Test 11: FAIL")

# Test 12
if is_right(9, 3, 4):
    print("Test 12: FAIL")
else:
    print("Test 12: PASS")
