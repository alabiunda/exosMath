def echangeLigne(A,i,j):
    lineStorage = A[j-1]
    A[j-1]=A[i-1]
    A[i-1]=lineStorage
    return A