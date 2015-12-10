import LinkedLists as LL
import solutions as sol
import Trees as T

def t1(): # test for problem 1
    A = LL.LinkedList()
    A.add(24)
    A.add(25)
    A.add(42)
    A.add(26)
    A.add(27)
    print A
    print sol.recursive_search(A, 42)

def t21(): # first test for problem 2
    """First test for problem 2 in Trees.py
    Output:
        [4]
        [3, 6]
        [5, 7, 8]
        [1]
    """
    B = T.BST()
    B.insert(4)
    B.insert(3)
    B.insert(6)
    B.insert(5)
    B.insert(7)
    B.insert(8)
    B.insert(1)

    print B

def t22():
    """Second test for problem 2 in Trees.py
    Output:
        [5]
        [3, 6]
        [1, 4, 9]
        [2, 7]
        [8]

        <ValueError> 4 is already in list
    """
    B = T.BST()
    B.insert(5)
    B.insert(6)
    B.insert(9)
    B.insert(3)
    B.insert(7)
    B.insert(1)
    B.insert(8)
    B.insert(2)
    B.insert(4)
    
    print B

    B.insert(4)

def t23():
    """Third test for problem 2 in Trees.py
    Output:
        [4]
        [2, 6]
        [1, 3, 5, 8]
        [7, 9]
    """
    B = T.BST()
    B.insert(4)
    B.insert(2)
    B.insert(1)
    B.insert(3)
    B.insert(6)
    B.insert(5)
    B.insert(8)
    B.insert(7)
    B.insert(9)

    print B

def t3():
    """First test for problem 3 in Trees.py
    Eventually all elements are eliminated.
    Output:
        [5]
        [3, 7]
        .
        .
        .
        [None]
    """
    C = T.BST()

    C.insert(5)
    C.insert(3)
    C.insert(2)
    C.insert(4)
    C.insert(7)
    C.insert(6)
    C.insert(8)

    print C

    C.remove(3)

    print C

    C.remove(4)
    print C
    C.remove(8)
    print C
    C.remove(7)
    print C
    C.remove(5)
    print C
    C.remove(6)
    print C
    C.remove(2)
    print C


