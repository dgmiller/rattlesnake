
# coding: utf-8

# In[5]:

# Extended Euclidean Algorithm

def gcd(a,b):
    if b == 0:
        return [1,0,a] # this implies ax + by = gcd(a,b) with x = 1 and y = 0.
    else:
        x,y,r = gcd(b,a%b) # backsubstituting produces these values.
        return [y, x - (a//b)*y, r] # we return a new ax + by = gcd(a,b).        


# In[12]:

a = 240
b = 7
x,y,denom = gcd(a,b)
print "gcd(%d,%d) = ax + by = %d(%d) + %d(%d) = %d" % (a, b, a, x, b, y, denom)


# In[13]:

a = 132
b = 8
x,y,denom = gcd(a,b)
print "gcd(%d,%d) = ax + by = %d(%d) + %d(%d) = %d" % (a, b, a, x, b, y, denom)


# In[17]:

a = 26
b = 144
x,y,denom = gcd(a,b)
print "gcd(%d,%d) = ax + by = %d(%d) + %d(%d) = %d" % (a, b, a, x, b, y, denom)


# In[18]:

a = 243
b = 12
x,y,denom = gcd(a,b)
print "gcd(%d,%d) = ax + by = %d(%d) + %d(%d) = %d" % (a, b, a, x, b, y, denom)


# In[ ]:



