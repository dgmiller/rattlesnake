"""
Student Module test
"""
import sys
import sample_test as sam
import StringIO

oldstdin = sys.stdin
sys.stdin = StringIO.StringIO('1\n5 2 1 9 6')
sam.probA()


