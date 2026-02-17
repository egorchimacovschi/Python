print(2 > 1)
print ("Hello wrold")
isar = True
print(isar)

string3 = "egor \"salut" #\ escapation
print (len(string3))
print(string3[0])
print(string3[-1])
print(string3[0:3])
print(string3[0:])

first = "egor"
last = "chimacovschi"
full = f"{first}  is {2+2}" #in{} u can put ealuated expresions
print (full)
full = first + " " + last
print(full)

course = "Python Programing"
print(course.upper())
print(course.title())
print(course.strip())
print(course.find("Pro"))
print(course.replace("P", "j"))
print("pro" in course)

print(10 + 3)
print(10 - 3)
print(10 * 3)
print(10 / 3)
print(10 // 3)
print(10 % 3)
print(10 ** 3)

x = 0
x += 1
print(x)

x = -2.39

print(round(x))
print(abs(x)) 
import math

print(math.ceil(2.2))

y = input()
#print(int(y)+1)
print(f"x: {y}, este de tip : {type(y)}")