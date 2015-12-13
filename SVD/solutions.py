# solutions.py
'''
Name: Derek Miller
Image Compression (SVD)
'''

from scipy import linalg as la
import numpy as np
from matplotlib import pyplot as plt
from matplotlib import cm

# Problem 1
def truncated_svd(A,r=None,tol=10**-6):
    """Computes the truncated SVD of A. If r is None or equals the number 
        of nonzero singular values, it is the compact SVD.
    Parameters:
        A: the matrix
        r: the number of singular values to use
        tol: the tolerance for zero
    Returns:
        U - the matrix U in the SVD
        s - the diagonals of Sigma in the SVD
        Vh - the matrix V^H in the SVD
    """
    m,n = A.shape
    AhA = np.dot(A.conj().T,A)
    s,V = la.eig(AhA) # this returns the eigvals and eigvecs
    # sort the eigenvalues and eigenvectors
    indices = np.argsort(s)
    s = s[indices][::-1]
    V = V[:,indices][:,::-1] # the eigvecs are stored as columns
    s = np.sqrt(s)
    s[s < tol] = 0
    #num_zero = len(s) - len(np.nonzero(s))

    if r == None:
        try:
            r = len(np.nonzero(s)[0])
            s = s[:r]
            V = V[:,:r]
        except:
            r = len(s)
    elif r <= 0:
        raise ValueError('r must be a positive integer')
    else:
        s = s[:r]
        V = V[:,:r]
    U = np.zeros((m,r))
    for i in range(r):
        U[:,i] = np.dot(A, V[:,i])/s[i]

    return U,np.diag(s),V.conj().T # U is (2x3) matrix with [:,2] = nan


# Problem 2
def visualize_svd():
    """Plot each transformation associated with the SVD of A."""
    unit_vec = np.load('circle.npz')['unit_vectors']
    circ = np.load('circle.npz')['circle']
    A = np.array([[3,1],[1,3]])
    U,E,Vh = la.svd(A)
    E = np.diag(E)
    c1 = np.dot(Vh,circ)
    v1 = np.dot(Vh,unit_vec)
    c2 = np.dot(E,c1)
    v2 = np.dot(E,v1)
    c3 = np.dot(U,c2)
    v3 = np.dot(U,v2)

    plt.subplot(221)
    plt.plot(unit_vec[0],unit_vec[1],circ[0],circ[1])
    plt.subplot(222)
    plt.plot(v1[0],v1[1],c1[0],c1[1])
    plt.subplot(223, aspect='equal')
    plt.plot(v2[0],v2[1],c2[0],c2[1])
    plt.subplot(224)
    plt.plot(v3[0],v3[1],c3[0],c3[1])
    plt.show()



# Problem 3
def svd_approx(A, k):
    """Returns best rank k approximation to A with respect to the induced 2-norm.
    
    Inputs:
    A - np.ndarray of size mxn
    k - rank 
    
    Return:
    Ahat - the best rank k approximation
    """
    U,s,Vh = la.svd(A, full_matrices=False)
    S = np.diag(s[:k])
    Ahat = U[:,:k].dot(S).dot(Vh[:k,:])
    return Ahat #la.norm(A-Ahat)
    
# Problem 4
def lowest_rank_approx(A,e):
    """Returns the lowest rank approximation of A with error less than e 
    with respect to the induced 2-norm.
    
    Inputs:
    A - np.ndarray of size mxn
    e - error
    
    Return:
    Ahat - the lowest rank approximation of A with error less than e.
    """
    U,s,Vh = la.svd(A, full_matrices=False)
    s[s<e] = 0
    return U.dot(np.diag(s)).dot(Vh)
    
# Problem 5
def compress_image(filename,k):
    """Plot the original image found at 'filename' and the rank k approximation
    of the image found at 'filename.'
    
    filename - jpg image file path
    k - rank
    """
    X = plt.imread(filename).astype(float)/255.
    C = X.copy()
    for i in xrange(3):
        C[:,:,i] = svd_approx(X[:,:,i],k)
    C[C > 1] = 1
    C[C <= 0] = 0
    plt.subplot(1,2,1)
    plt.imshow(X)
    plt.subplot(1,2,2)
    plt.imshow(C)
    plt.show()
    #output not showing correctly



### TEST FUNCTION ###

def test(x):
    A = np.array([[3.,2.,2.],[2.,3.,-2.]])
    if x == 1:
        print "PROBLEM 1\n"
        #U = [[.7071   .7071],  Vh = [[.7071   .7071   0.000],
        #     [.7071  -.7071]]        [.2357  -.2357   .9428], 
        #s = [5  3  0]                [.6666  -.6666  -.3333]]
        U,s,Vh = truncated_svd(A)
        #print "U = ", U
        #print "s = ", s
        #print "Vh = ", Vh
        Ahat = U.dot(s).dot(Vh)
        #print "Ahat = ", Ahat
        #print "A = ", A
        print np.allclose(A, Ahat)
        return U,s,Vh
    elif x == 2:
        print "PROBLEM 2\n"
        visualize_svd()
        #complete
    elif x == 3:
        print "PROBLEM 3\n"
        print svd_approx(A,1)
        #complete
    elif x == 4:
        print "PROBLEM 4\n"
        e = .1
        print lowest_rank_approx(A, e)
    elif x == 5:
        print "PROBLEM 5\n"
        compress_image('hubble_image.jpg', 15)
    else:
        print "Enter a number 1-5"




