t = (('blue', 'red'), 'yellow', 'navy blue', 'gray')
print(t)
print(t[0])
print(t[-1])
print(t[1:3])
print(t[:3])
print(t[1:])
print(t[-3:-1])
print(t[-2:])

for i in range(10):
    a = int(0)
    for j in range(10):
        a = a + j
        if a > 25:
            break
print(str(a))
