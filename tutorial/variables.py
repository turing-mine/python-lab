
# variables with no output
x = 5
y = "Hello, World!"

x = 4
y = "John"
print(x)
print(y)

x = 4 # x is of type int
x = "Sally" # x is now of type str
print(x)

z = "Bubba"
# is the same as
z = 'Bubba'

print(z)


#Legal variable names:
myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"

#Illegal variable names:
# 2myvar = "John"
# my-var = "John"
# my var = "John"

q, r, s = "Orange", "Banana", "Cherry"
print(q)
print(r)
print(s)

t = u = v = "Apple"
print(t)
print(u)
print(v)

x = "awesome"
print("Python is " + x)

x = "Python is "
y = "bueno"
z =  x + y
print(z)

x = 5
y = 10
print(x + y)

x = "cool"

def myfunc():
  print("Python is " + x)

myfunc()


d = "awesomeness"

def myfunc2():
  d = "fantasticness"
  print("Python is " + d)

myfunc2()

print("Python is " + d)


g = "awesome"

def myfunc3():
  global g
  g = "ketch"

myfunc3()

print("Python is " + g)

