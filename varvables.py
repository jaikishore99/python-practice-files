# variables syntax

x = 5

y = "kishore"

print(x)

print(y)

# int and str vars

x = 5  # int val

x = "jai"  # str var

print(x)

# duo str var #dou and single quots

x = "jai"

print(x)

x = 'kishore'

print(x)

# var names #legal var names

myvar = "prabhas"
my_var = "mahesh"
_my_var = "pavan"
myVar = "chiru"
MYVAR = "PRABHAS"
myvar2 = "2prabhas"

# mul vars

x, y, z = "banana", "orange", "apple"

print(x)

print(y)

print(z)

# assign same var vals

x = y = z = "orange"

print(x)

print(y)

print(z)

# output vars

x = "kishore"

print("jai" + x)

# + char vars

x = "jai"

y = "kishore"

z = x+y

print(z)

# + char math opert

x = 5

y = 5

print(x+y)

# combine str and var
#o = 5
#y ="kishore"
# print(x+y) # error output


# GLOBAL VARS

# function vars
x = "kishore"


def myfunc():
    print("jai " + x)


myfunc()

# function vars and vars

x = "awsome"


def myfunc():
    x = "jai"
    print("kishore" + x)


myfunc()

print("python is " + x)

# global x var


def myfunc():
    global x
    x = "baahubali"


myfunc()

print("prabhas in " + x)

# global x fun var and vars

x = "awsome"


def myfunc():
    global x
    x = "fantastic"


myfunc()

print("python is " + x)
