import math
import numpy
import numpy as np

M = np.array([[4.1,2.0,0],[4.6,1,6],[2,8,3]])

print (M[1][2]) #Affichage de l'élement M23
print (M[2]) #Affichage de la 3eme ligne
for i in range(np.shape(M)[0]):
    print (M[i][0]) #Affichage de la 1ere colonne
N = np.ones(9)
N = N.reshape((3,3))
O = np.diagflat([1.0,1.0,1.0,1.0,1.0])
print (O)
A = np.array([2,4,6,12,24,36])
A = A.reshape (3,2)
print (A)