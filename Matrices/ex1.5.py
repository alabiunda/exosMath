import math
import numpy as np
from multiply import multiply

A = np.array([[4.1,2.0,0],[4.6,1,6],[2,8,3]])
B = np.array([[1,1,0],[1.0,1,1],[2,2,2]])
C = np.array([[1,2],[0,1],[3,1]])

D = A*B
print (D) # Multiplication terme par terme
E = A@B
print (E) # Produit matriciel

print ('Le résultat de la multiplication de A par B ')
print (multiply(A,B))
print ('Le résultat de la multiplication de A par C ')
print (multiply(A,C))
print ('Le résultat de la multiplication de C par A ')
print (multiply(C,A))