"""
Student Module test
"""

import sys

def probA():
    T = raw_input()
    print "Number of test cases"
    print T
    for i in range(int(T)):
        n = raw_input()
        print "Number of candidates"
        print n
        print "votes"
        for j in range(int(n)):
            print raw_input()

def example():
    T = input()
    for i in xrange(T):
        arr = map(int, raw_input().strip().split())
        print sum(arr)
