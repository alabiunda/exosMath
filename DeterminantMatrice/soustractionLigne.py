#Attention, pour être fonctionnel, cette fonction requiert un objet de type np.array
def soustractionLigne(A,k,i,alpha):
    stockLigne = A[i-1]
    stockLigne = alpha*stockLigne
    stockLigne = (-1)*stockLigne
    A[k-1]=A[k-1]+stockLigne
    return A