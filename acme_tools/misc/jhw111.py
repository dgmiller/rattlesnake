# Standard Elementary School Subtraction

a = [7, 6, 5, 4]
a.reverse()
b = [6, 9, 8, 7]
b.reverse()
c = []

while len(b) < len(a):
    b.append(0)

for x in range(len(b)):
    if a[x] >= b[x]:
        c.append(a[x]-b[x])
    else:
        a[x] = a[x] + 10
        a[x+1] = a[x+1] - 1
        c.append(a[x]-b[x])

c.reverse()

print c

