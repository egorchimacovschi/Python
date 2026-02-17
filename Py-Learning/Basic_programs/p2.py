x, y = 2, 3
z = "Egor"
print(x, y)
x, y = y, x
print(x, y)
print(z)
print("1"+str(2))

t = 1
p = 0
print(t or p)
print("Un sir:", "3" + "5") # Un sir: 35
print("Un numar:", 4 % 3 + int("41")) # Un numar: 42
print("Un sir:", "3" + str(5)) # Un sir: 35
print("student %s are nota %d"%("X",10)) # student X are nota 10
print((2.0 + 3.0j) * (2.1 - 6.0j)) # (22.2-5.7j)
print(2 ** 3 ) # 8

egor = """egor
salut"""
print (egor)
egor = "egor"
print (egor[-4])
print (len(egor))
ion = ''
ion = egor[0:3]
print (ion) #stringurile nu pot fi modificate
print (egor + ion) #concatenarea
print (egor*2) #multiplicate
print ("%s"%(egor)) # poate facut ca in c

s = "string"
print(s[0:2]) # st
print(s[:3]) # str
print(s[3:]) # ing
s2 = "un "
print("Scrie " + 2*s2 + s)
# Scrie un un string
print("hello %s, lab %d !" % ("studenti",14))
# hello studenti, lab 14 !
import string
print("hello {}, lab {}".format("world",14))
# hello world, lab 14