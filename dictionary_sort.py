L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
D1 = {"Bob":75,"Adam":92,"bart":66,"Lisa":88}
L2 = D1.items()

print("dict to list: ")
print(L2)

def by_name(t):
    return t[1]

L3 = sorted(L2, key=by_name)
print("after sorting:")
print(L3)

print("back to dictionary:")
print(dict(L2))

L4 = sorted(D1.items(),key=lambda x:x[1])
print("using lambda:")
print(L4)
 
