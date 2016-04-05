print("list")
a = [1, 2, 3]
for index, item in enumerate(a):
    print index, item    

print("tuple")
b = (1, 2, 3)
for index, item in enumerate(b):
    print index, item

print("dictionary")
c = {'a':1, 'b':2, 'c':3}
for index, item in enumerate(c):
    print index, item


print("string")
d = "hello world"
for index, item in enumerate(d):
    print index, item
