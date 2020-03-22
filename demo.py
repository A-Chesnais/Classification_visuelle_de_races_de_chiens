# -*- coding: utf-8 -*-
"""
Created on Sun Jan 19 13:07:59 2020

@author: Antoine
"""

from tkinter import *
import pandas as pd
import numpy as np
from PIL import ImageTk
from keras.preprocessing.image import load_img, img_to_array
from tensorflow.keras.models import load_model
from tensorflow.keras import applications

# Chargement du modele Keras
tl_model = load_model('resultats/modeles_retenus/trl_classifier_inception.h5')

# Chargement du mapping numero de classe / race de chien
labels = pd.read_csv('demo_data/dog_breed_mapping.csv', index_col='key')

# Fonction activee lors de l'appui sur le boutton
# "Predire la race"
def predict():
    
   global img_tk
    
   # Recupere le nom du chien (fichier) pour lequel faire une prediction
   file_loc = E1.get()
   
    # Chargement de l'image du chien
   img = load_img('demo_data/images/' + file_loc + '.jpg')
   width, height = img.size
   
   # Preprocessing de l'image
   preprocessed_img = applications.inception_v3.preprocess_input(img_to_array(img))
   preprocessed_img = np.expand_dims(preprocessed_img, axis=0)  
   
   # Prediction des pobabilites pour chaque classe
   # et choix de la classe la plus probable
   prediction = tl_model.predict(preprocessed_img)
   breed_prob = prediction.max()
   breed_pred = labels.loc[np.argmax(prediction, axis=1)[0], 'breed']
   print(breed_pred)
   
   # Conversion de l'image du chien en format utilise par TKinter
   img_tk = ImageTk.PhotoImage(img)
   # Creation de la fenetre qui contiendra l'image du chien
   image_display = Toplevel(fenetre)
   
   # Affichage de l'image choisie
   canvas = Canvas(image_display, width = width, height = height)
   canvas.create_image((0, 0),anchor=NW, image=img_tk)
   canvas.pack(side = BOTTOM, padx=5, pady=5)

   # Affichage de la prediction de la race au dessus de l'image
   L2_text = file_loc + ' est probablement un ' + breed_pred + ' (p = ' + str(breed_prob)[:4] + ')'
   L2 = Label(image_display, text=L2_text)
   L2.pack( side = TOP, padx=5, pady=5)

# Creation de la fenetre principale de l'interface
fenetre = Tk()

L1 = Label(fenetre, text = "Nom du chien")
L1.pack( side = LEFT)

B = Button(fenetre, text = "Predire la race", command = predict)
B.pack(side = RIGHT)

file_loc = StringVar()
file_loc.set('hector')
E1 = Entry(fenetre, textvariable=file_loc , bd = 3, width=30)
E1.pack(side = RIGHT)



fenetre.mainloop()
