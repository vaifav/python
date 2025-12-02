import copy

a = [1,2,[3,4]]
b = a.copy()
c = copy.deepcopy(a)

b[2].append(10)
c[2].append(20)

print(a)
print(b)
print(c)