#-*- coding: utf8 -*-

# La première ligne indique le type d'encodage utilisé.

#----------------------------------------------------------------------#
#                                                                      #
#                 Cours de Mathématiques pour BAC Info                 #
#                            G. Barmarin                               #
#                                                                      #
#----------------------------------------------------------------------#

#-----------------------------------------------------------------------
# Importation des bibliothèques
#-----------------------------------------------------------------------

import time
from tkinter import *
from PIL import Image, ImageTk
import numpy as np
import math

#-----------------------------------------------------------------------
# encodage des fonctions
#-----------------------------------------------------------------------

#-----------------------------------------------------------------------
# encodage du programme principal
#-----------------------------------------------------------------------

print("Utilisation de numpy, de PIL et de tkinter")
print("------------------------------------------")
print("Utilisation des arrays pour traiter des images\n")
print("et de tkinter pour les afficher\n")

# On charge l'image et on la transforme en tableau (dé-commenter le format qui vous intéresse)

#nom="6x2.png"
#nom="6x2.gif"
#nom="6x2.tif"
nom="4-2-03.png"
nom2="Lenna512.png"
#nom="6x2.jpg"


image_entree = Image.open(nom)
image_entree2 = Image.open(nom2)
image = np.asarray(image_entree)
image2 = np.asarray(image_entree2)
nb_lignes = image.shape[0]
nb_colonnes = image.shape[1]
nb_tab = image.shape[2]
print
print("\nVous avez ouvert l'image ", nom)
print("qui a pour dimensions ", nb_lignes,"lignes et ", nb_colonnes, " colonnes\n")
print("Voici ce que le tableau numpy contient:\n")

# On affiche le tableau numpy représentant l'image

#-----------------------------------------------------------------------
# Traitement de l'image
#-----------------------------------------------------------------------

start = time.time()			# stocke l'heure du démarrage du traitement

imageStockage = np.copy(image)
imageStockage2 = np.copy(image2)

imageStockage = imageStockage * 0.6
imageStockage2 = imageStockage2 * 0.4

image_sortie = (imageStockage + imageStockage2)

for tab in range(nb_tab):
    for ligne in range(nb_lignes):
        for colonne in range(nb_colonnes):
            image_sortie[ligne][colonne][tab] = int(round(image_sortie[ligne][colonne][tab]))
            if image_sortie[ligne][colonne][tab] > 255:
                image_sortie[ligne][colonne][tab] = 255

image_sortie=image_sortie.astype(np.uint8)

end = time.time()			# stocke l'heure de la fin du traitement

print("\nEt voici ce que le tableau de sortie contient:\n")

print ("\nDurée du traitement: ",end - start, " seconde\n")	# Affichage du temps d'éxécution du traitement

# On sauvegarde les images pour pouvoir les afficher

Image.fromarray(image).save("image_entree.png")
Image.fromarray(image_sortie).save("image_sortie.png")

#-----------------------------------------------------------------------
# Affichage dans tkinter
#-----------------------------------------------------------------------

# création de la fenêtre
root=Tk()
# Affichage d'une ligne blanche
empty_line0 = Label(root, text="")
empty_line0.pack()
# Affichage d'une ligne de texte
titre_line00 = Label(root, text="LABO COURS DE MATH: TRAITEMENT D'IMAGES")
titre_line00.pack()
# Affichage d'une ligne de texte
champ_label_result0 = Label(root, text="On affiche l'image avant transformation et après")
champ_label_result0.pack()
empty_line2 = Label(root, text="")
empty_line2.pack()
# Affichage d'une ligne de texte
champ_label_result1 = Label(root, text="Image avant transformation")
champ_label_result1.pack()
# Préparation de l'affichage de l'image avant transformation
image_in = Image.open("image_entree.png")
photo = ImageTk.PhotoImage(image_in)
# Préparation de l'affichage de l'image après transformation
image_out = Image.open("image_sortie.png")
photo2 = ImageTk.PhotoImage(image_out)
# Création d'un canevas et affichage de l'image dedans
canvas = Canvas(root,width=300,height=250,bg="silver")
canvas.create_image(150,127, image=photo)
canvas.pack()
# Affichage d'une ligne de texte
champ_label_result2 = Label(root, text="Image après transformation")
champ_label_result2.pack()
# Création d'un canevas et affichage de l'image dedans
canvas = Canvas(root,width=300,height=250,bg="silver")
canvas.create_image(150,127, image=photo2)
canvas.pack()
# Affichage d'une ligne blanche
empty_line3 = Label(root, text="")
empty_line3.pack()
# Affichage d'un bouton pour quitter/fermer la fenêtre
bouton_valider = Button(root, text="Quit", command=root.destroy)
bouton_valider.pack()
# Affichage d'une ligne blanche
empty_line4 = Label(root, text="")
empty_line4.pack()
# Lancement de la boucle d'affichage
root.mainloop()
