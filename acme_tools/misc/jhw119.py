print "PROBLEM 9: computing for example 1.1.19\n"

# verify the true solution
a = 450
b = 40545
c = 50
d = 70226
e = 702260

n1 = a * (b ** 4)
n2 = c * (d ** 4)
n3 = e ** 2

ans = (n1 - n2 + n3) / 10.**4
print ans

# verify the floating point solution

x = 4054.5 ** 4
y = 7022.6 ** 4
z = 7022.6 ** 2

sol = (450 * x) - (50 * y) + z
print sol

print "\nPROBLEM 10\n"

x = 2. ** 53 + 1
print (x-3) % 2
print (x-2) % 2
print (x-1) % 2
print (x % 2)
print x

print "\nPROBLEM 11\n"

X = .1
Y = .2
Z = X + Y
print Z
Z = 1/.3
print Z 

print "\nPROBLEM 12\n"

print(sum((1./n**6 for n in xrange(1,1001))))
print(sum((1./n**6 for n in xrange(1000,0,-1))))

