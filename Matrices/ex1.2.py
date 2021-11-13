import math

A = [[1,2,3],[4,5,6],[7,8,9]]
B = [[9,9,9],[9,9,9],[9,9,9]]
X = [[0,0,0],[0,0,0],[0,0,0]]
AB = A+B
for i in range(3):
    for j in range (3):
        X[i][j] = A[i][j]+B[i][j]

print (A)
print (B)
print (AB) #Calcule A+B et l'affiche -> La liste B a été ajoutée à la suite de la liste A
print (X) #Addition de A et B suivant les regles du calcul matriciel
