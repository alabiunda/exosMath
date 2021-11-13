import numpy as np
from multiply import multiply

def entryMatrice():
    colMat1 = int(input("Nombre de Colonnes de la 1ere matrice :"))
    ligMat1 = int(input("Nombre de Lignes de la 1ere matrice :"))
    colMat2 = int(input("Nombre de Colonnes de la 2eme matrice :"))
    ligMat2 = int(input("Nombre de Lignes de la 2eme matrice : "))

    mat1 = np.zeros((ligMat1,colMat1))
    mat2 = np.zeros((ligMat1,colMat1))
    for i in range(ligMat1):
        for j in range (colMat1):
            mat1[i][j] = float(input("Matrice 1 : Entrez la valeur située sur la ligne numero " +  str(i+1) + " et sur la colonne numero " + str(j+1)))
    for i in range(ligMat2):
        for j in range (colMat2):
            mat2[i][j] = float(input("Matrice 2 : Entrez la valeur située sur la ligne numero " +  str(i+1) + " et sur la colonne numero " + str(j+1)))
    choice = 7

    while choice != 0:
        print("Que voulez vous faire avec ces 2 matrices ?")
        print("1. Produit matriciel de la 1ere par la 2eme")
        print("2. Produit matriciel de la 2eme par la 1ere")
        print("3. Somme des 2 matrices")
        print("4. Transposée de la 1ere matrice et affichage du nombre de lignes et colonnes")
        print("Si vous voulez quitter ce programme, entrez 0")
        choice = int(input("Entrez le nombre correspondant à votre choix :"))
        if choice == 1:
            print("Produit matriciel de la 1ere par la 2eme est ")
            print(multiply(mat1,mat2))
        elif choice == 2:
            print("Produit matriciel de la 2eme par la 1ere")
            print(multiply(mat2,mat1))
        elif choice == 3:
            if np.shape(mat1) == np.shape(mat2) :
                print ("Somme des 2 matrices")
                print (mat1+mat2)
            else :
                print ("La taille des 2 matrices n'étant pas identiques, elles ne peuvent pas être additionnées")
        elif choice == 4:
            traMat1 = np.zeros((colMat1,ligMat1))
            for i in range(ligMat1):
                for j in range(colMat1):
                    traMat1[j][i] = mat1[i][j]
            print("La transposée de la 1ere matrice est la matrice suivante : ")
            print(traMat1)
