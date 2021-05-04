import numpy as np
import numpy.linalg as npla

def LU(A,f):
    # get the size of the system
    n = len(f)
    
    # check the size
    
    if (A.shape[0] != n) or (A.shape[1] != n):
      print('\t Inconsistent size in LU decomposition')
      info = 0
      return M,info

    # create the augmented matrix
    M = np.zeros((n,n+1))
    M[:,:-1] = A
    M[:,-1] = f

    # loop through all the colum
    # to get rid of the lower part
    for iC in range(n-1):
      # for each column loop over all the lines
      # that are below the diagonal
      # to set to 0 their elements
      for iL in range(iC+1,n):
        # check if the diagonal element
        # is null
        if(M[iC,iC] == 0):
          print('\t Zero on the diagonal, LU failed')
          info = 0
          return M,info
        # eliminate the element
        M[iL,:] = M[iL,:] - M[iL,iC]/M[iC,iC] * M[iC,:]

    # if we succed we return info = 1 and the upper augmetned matrix

    info = 1
    return M,info

def BS(M):
    ########################################################
    # Function to backsubstitute the results
    # and get the final solution
    ########################################################
    
    # get the size of the matrix
    n = M.shape[0]
    # loop over all the lines
    # starting by the end
    for iL in range(n-1,-1,-1):
      # check if we have diagonal elements on the diagonal
      if(M[iL,iL] == 0):
        print('\t Zero on the diagonal, LU failed')
        info = 0
        return M,info
      # divide the line by the diagonal element of M
      M[iL,:] /= M[iL,iL]
      
      # loop over all the lines that are above this onef
      for iLL in range(iL-1,-1,-1):
        M[iLL,:] -= M[iLL,iL]*M[iL,:]

    info = 1
    x=M[:,n]
    return x,info


