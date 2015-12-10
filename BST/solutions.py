# name this file 'solutions.py'
"""Volume II Lab 5: Data Structures II (Trees)
Derek Miller
Vol 2
15 Oct 2015
"""

from Trees import BST
from Trees import AVL
import numpy as np
import WordList
import time
import LinkedLists as LL
from matplotlib import pyplot as plt

def iterative_search(linkedlist, data):
    """Find the node containing 'data' using an iterative approach.
    If there is no such node in the list, or if the list is empty,
    raise a ValueError with error message "<data> is not in the list."
    
    Inputs:
        linkedlist (LinkedList): a linked list object
        data: the data to find in the list.
    
    Returns:
        The node in 'linkedlist' containing 'data'.
    """
    # Start the search at the head.
    current = linkedlist.head
    
    # Iterate through the list, checking the data of each node.
    while current is not None:
        if current.data == data:
            return current
        current = current.next
    
    # If 'current' no longer points to a Node, raise a value error.
    raise ValueError(str(data) + " is not in the list.")


# Problem 1: rewrite iterative_search() using recursion.
def recursive_search(linkedlist, data):
    """Find the node containing 'data' using a recursive approach.
    If there is no such node in the list, raise a ValueError with error
    message "<data> is not in the list."
    
    Inputs:
        linkedlist (LinkedList): a linked list object
        data: the data to find in the list.
    
    Returns:
        The node in 'linkedlist' containing 'data'.
    """
    def curseme(current, data):
        if current is None:
            raise ValueError(str(data) + " is not in the list.")

        if current.data == data:
            return current
        else:
            return curseme(current.next, data)
    return curseme(linkedlist.head, data)

# Problem 2: Implement BST.insert() in Trees.py.


# Problem 3: Implement BST.remove() in Trees.py


# Problem 4: Test build and search speeds for LinkedList, BST, and AVL objects.
def plot_times(filename="English.txt", start=500, stop=5500, step=500):
    """Vary n from 'start' to 'stop', incrementing by 'step'. At each
    iteration, use the create_word_list() from the 'WordList' module to
    generate a list of n randomized words from the specified file.
    
    Time (separately) how long it takes to load a LinkedList, a BST, and
    an AVL with the data set.
    
    Choose 5 random words from the data set. Time how long it takes to
    find each word in each object. Calculate the average search time for
    each object.
    
    Create one plot with two subplots. In the first subplot, plot the
    number of words in each dataset against the build time for each object.
    In the second subplot, plot the number of words against the search time
    for each object.
    
    Inputs:
        filename (str): the file to use in creating the data sets.
        start (int): the lower bound on the sample interval.
        stop (int): the upper bound on the sample interval.
        step (int): the space between points in the sample interval.
    
    Returns:
        Show the plot, but do not return any values.
    """
    Liszt = WordList.create_word_list(filename)
    Atimes = []
    Btimes = []
    Ctimes = []
    Alist = []
    Blist = []
    Clist = []

    for n in range(start, stop, step):
        A = LL.LinkedList()
        B = BST()
        C = AVL()

        begin = time.time()
        for word in Liszt[:n]:
            A.add(word)
        end = time.time()
        timedA = end - begin
        Atimes.append(timedA)

        begin = time.time()
        for word in Liszt[:n]:
            B.insert(word)
        end = time.time()
        timedB = end - begin
        Btimes.append(timedB)

        begin = time.time()
        for word in Liszt[:n]:
            C.insert(word)
        end = time.time()
        timedC = end - begin
        Ctimes.append(timedC)
        timed = end - begin

        random_numbers = np.random.randint(0, n, 5)

        for number in random_numbers:
            word = Liszt[number]

            begin = time.time()
            iterative_search(A, word)
            end = time.time()
            timedA = end - begin
            Alist.append(timedA)

            begin = time.time()
            B.find(word)
            end = time.time()
            timedB = end - begin
            Blist.append(timedB)

            begin = time.time()
            C.find(word)
            end = time.time()
            timedC = end - begin
            Clist.append(timedC)

    #plt.subplot(121)
    plt.title("Build Times")
    plt.plot(range(start, stop, step), Atimes, Btimes, Ctimes)

    #plt.subplot(122)
    #plt.title("Search Times")
    #plt.plot(range(start, stop, step), Alist, Blist, Clist)

    plt.show()



# =============================== END OF FILE =============================== #

