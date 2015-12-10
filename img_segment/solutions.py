# name this file solutions.py
"""Volume I Lab 10: 
Derek Miller
Image Segmentation
"""
from scipy import linalg as la
from scipy import sparse
from scipy.sparse import linalg as spla
import numpy as np
from matplotlib import pyplot as plt

# Helper function for computing the adjacency matrix of an image
def getNeighbors(index, radius, height, width):
    '''
    Calculate the indices and distances of pixels within radius
    of the pixel at index, where the pixels are in a (height, width) shaped
    array. The returned indices are with respect to the flattened version of the
    array. This is a helper function for adjacency.
    
    Inputs:
        index (int): denotes the index in the flattened array of the pixel we are 
                looking at
        radius (float): radius of the circular region centered at pixel (row, col)
        height, width (int,int): the height and width of the original image, in pixels
    Returns:
        indices (int): a flat array of indices of pixels that are within distance r
                   of the pixel at (row, col)
        distances (int): a flat array giving the respective distances from these 
                     pixels to the center pixel.
    '''
    # Find appropriate row, column in unflattened image for flattened index
    row, col = index/width, index%width
    # Cast radius to an int (so we can use arange)
    r = int(radius)
    # Make a square grid of side length 2*r centered at index
    # (This is the sup-norm)
    x = np.arange(max(col - r, 0), min(col + r+1, width))
    y = np.arange(max(row - r, 0), min(row + r+1, height))
    X, Y = np.meshgrid(x, y)
    # Narrows down the desired indices using Euclidean norm
    # (i.e. cutting off corners of square to make circle)
    R = np.sqrt(((X-np.float(col))**2+(Y-np.float(row))**2))
    mask = (R<radius)
    # Return the indices of flattened array and corresponding distances
    return (X[mask] + Y[mask]*width, R[mask])

# Helper function used for testing connectivity in problem 2.
def sparse_generator(n, c):
    ''' Return a symmetric nxn matrix with sparsity determined by c.
    Inputs:
        n (int): dimension of matrix
        c (float): a float in [0,1]. Larger values of c will produce
            matrices with more entries equal to zero.
    Returns:
        sparseMatrix (array): a matrix defined according the n and c
    '''
    A = np.random.rand(n**2).reshape((n, n))
    A = ( A > c**(.5) )
    return A.T.dot(A)

# Helper function used to display the images.
def displayPosNeg(img_color,pos,neg):
    '''
    Displays the original image along with the positive and negative
    segments of the image.
    
    Inputs:
        img_color (array): Original image
        pos (array): Positive segment of the original image
        neg (array): Negative segment of the original image
    Returns:
        Plots the original image along with the positive and negative
            segmentations.
    '''
    plt.subplot(131)
    plt.imshow(neg)
    plt.subplot(132)
    plt.imshow(pos)
    plt.subplot(133)
    plt.imshow(img_color)
    plt.show()

# Helper function used to convert the image into the correct format.
def getImage(filename='dream.png'):
    '''
    Reads an image and converts the image to a 2-D array of brightness
    values.
    
    Inputs:
        filename (str): filename of the image to be transformed.
    Returns:
        img_color (array): the image in array form
        img_brightness (array): the image array converted to an array of
            brightness values.
    '''
    img_color = plt.imread(filename)
    img_brightness = (img_color[:,:,0]+img_color[:,:,1]+img_color[:,:,2])/3.0
    return img_color,img_brightness


# Problem 1: Implement this function.
def laplacian(A):
    '''
    Compute the Laplacian matrix of the adjacency matrix A.
    Inputs:
        A (array): adjacency matrix for undirected weighted graph,
             shape (n,n)
    Returns:
        L (array): Laplacian matrix of A
        
    '''
    d = np.array()
    for row in A:
        d.append(sum(row))
    D = np.diag(d)
    return D-A

# Problem 2: Implement this function.
def secondEigenvalue(A):
    '''
    Compute the second smallest eigenvalue of the adjacency matrix A.
    Inputs:
        A (array): adjacency matrix for undirected weighted graph,
             shape (n,n)
    Returns:
        lambda (float): the second of the eigenvalues of L, when they
            arranged least to greatest.  Only return the real part.
    '''
    L = laplacian(A) # the laplacian matrix D-A
    evals = la.eigh(L,eigvals_only=True) # eigenvalues of L
    return evals[-2]

# Problem 3: Implement this function.
def adjacency(img_brightness, radius = 5.0, sigma_I = .15, sigma_d = 1.7):
    '''
    Compute the weighted adjacency matrix for
    the image given the radius. Do all computations with sparse matrices.
    Also, return an array giving the main diagonal of the degree matrix.
    
    Inputs:
        img_brightness (array): array of brightnesses given by the function getImage()
        radius (float): maximum distance where the weight isn't 0
        sigma_I (float): some constant to help define the weight
        sigma_d (float): some constant to help define the weight
    Returns:
        W (sparse array(csc)): the weighted adjacency matrix of img_brightness,
            in sparse form.
        D (array): 1D array representing the main diagonal of the degree matrix.
    '''
    height = img_brightness.shape[0]
    width = img_brightness.shape[1]
    Adj_size = height*width
    img_bright = img_brightness.flatten()
    W = sparse.lil_matrix((Adj_size,Adj_size))
    D = np.zeros(Adj_size)
    for i in range(Adj_size):
        # indices surrounding a pixel with a given distance
        ind,dist = getNeighbors(i,radius,height,width)
        # we only need the indices from int_dist
        for p,d in zip(ind,dist): # p is an
            I = np.absolute(img_bright[i] - img_bright[p])
            W[i,p] = np.exp(-I/sigma_I**2 - d/sigma_d**2)
        D[i] += W[i].sum()
    W = sparse.csc_matrix(W)
    return W,D

# Problem 4: Implement this function.
def segment(img_brightness):
    '''
    Compute and return the two segments of the image as described in the text. 
    Compute L, the laplacian matrix. Then compute D^(-1/2)LD^(-1/2),and find
    the eigenvector corresponding to the second smallest eigenvalue.
    Use this eigenvector to calculate a mask that will be usedto extract 
    the segments of the image.
    Inputs:
        img_brightness (array): an array of brightnesses given by the function
            getImage().
    Returns:
        seg1 (array): an array the same size as img_brightness, but with 0's
                for each pixel not included in the positive
                segment (which corresponds to the positive
                entries of the computed eigenvector)
        seg2 (array): an array the same size as img_brightness, but with 0's
                for each pixel not included in the negative
                segment.
    '''
    m,n = img_brightness.shape
    img_bright = img_brightness.flatten()
    W,D = adjacency(img_brightness)
    new_D = 1./np.sqrt(D)
    D = sparse.spdiags(D,0,W.shape[0],W.shape[1])
    new_D = sparse.spdiags(new_D,0,W.shape[0],W.shape[1])
    L = D-W
    DLD = (new_D.dot(L)).dot(new_D)
    e_vals, e_vecs = spla.eigs(DLD,which='SR')
    M = e_vecs[:,1] # the eigvec -> second smallest eigvalue
    M_pos = np.zeros_like(M)
    M_neg = np.zeros_like(M)
    for i in xrange(M.shape[0]):
        if M[i] > 0:
            M_pos[i] = img_bright[i]
        elif M[i] < 0:
            M_neg[i] = img_bright[i]
    M_pos = np.real(M_pos)
    M_neg = np.real(M_neg)
    return np.reshape(M_pos, (m,n)), np.reshape(M_neg, (m,n))




