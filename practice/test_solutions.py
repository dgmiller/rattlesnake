import numpy as np
import StringIO
import sys
import sample_test

n = "10\n"
t1 = "3\n10\n21\n10\n"
t2 = "3\n20\n10\n10\n"
t3 = "3\n10\n10\n10\n"
t4 = "4\n15\n15\n15\n45\n"
t5 = "5\n7\n500\n600\n1\n50000\n"
t6 = "6\n50000\n50000\n50000\n50000\n50000\n50000\n"
t7 = "10\n0\n0\n0\n0\n0\n0\n0\n1\n0\n0\n"
t8 = "2\n0\n1\n"
t9 = "8\n25\n26\n30\n24\n23\n27\n28\n29"
    
to_test = n+t1+t2+t3+t4+t5+t6+t7+t8+t9

oldstdin = sys.stdin
sys.stdin = StringIO.StringIO(to_test)
student_output = sample_test.probA()

t1out = "majority winner 2\n"
t2out = "minority winner 1\n"
t3out = "no winner\n"
t4out = "minority winner 4\n"
t5out = "majority winner 5\n"
t6out = "no winner\n"
t7out = "majority winner 8\n"
t8out = "majority winner 2\n"
t9out = "minority winner 3"

test_output = t1out + t2out + t3out + t4out + t5out + t6out + t7out + t8out + t9out

if student_output == test_output:
    print("correct")
else:
    print("failed")
