a = ('apple', 'banana', 'cherry')
b = "Hello World"
c = 33

x = type(a)
y = type(b)
z = type(c)

print(x)  # <class 'tuple'>
print(y)  # <class 'str'>
print(z)  # <class 'int'>

if z == int:
    print("yes")
else:
    print("no")
