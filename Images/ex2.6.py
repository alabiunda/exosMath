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
nom="Lenna512.bmp"
#nom="6x2.jpg"


image_entree = Image.open(nom)
image = np.asarray(image_entree)
nb_lignes = image.shape[0]
nb_colonnes = image.shape[1]
print
print("\nVous avez ouvert l'image ", nom)
print("qui a pour dimensions ", nb_lignes,"lignes et ", nb_colonnes, " colonnes\n")
print("Voici ce que le tableau numpy contient:\n")

# On affiche le tableau numpy représentant l'image

#-----------------------------------------------------------------------
# Traitement de l'image
#-----------------------------------------------------------------------

start = time.time()			# stocke l'heure du démarrage du traitement

image_sortie=image# ici on recopie simplement l'image d'entrée dans celle de sortie
blue = [[0,0,0],[0,0,0],[0,0,1]]

image_sortie = np.matmul(image,blue)

print(np.shape(image))
print(np.shape(image_sortie))
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
