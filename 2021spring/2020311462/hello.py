a, b, s = 1, 0, 0
list0 = []
while True:
    s = a + b
    list0.append(s)
    b = a
    a = s
    if list0.__len__() > 1000:
        break
print(list0)
x = 1
for i in range(0, 1000):
    x *= list0[i]
print(x)
