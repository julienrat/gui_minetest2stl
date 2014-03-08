#!/usr/bin/env python3
# -*- coding: utf-8 -*-


#interface de conversion Minetest to STL
#dependances python-tk, openscad, python3
# Licence GNU-GPL
# Julien RAT pour les Petits Debrouillards et les amis

from tkinter import *
import tkinter.filedialog
import subprocess
myFormats = [
    ('Fichier STL','*.stl'),   
    ]
def Ouvrir():
	file_path = tkinter.filedialog.askdirectory()
	var.set(str(file_path))    
	fen1.update_idletasks()
	
def Enregistrer():
	file2_path = tkinter.filedialog.asksaveasfile(mode='w',filetypes=myFormats ,title="Enregistrer le fichier STL sous ...") #tkFileDialog.asksaveasfilename(**self.file_opt)
	cible.set(str(file2_path.name))    
	fen1.update_idletasks()

def Convertir():
	print("./minetestmapper.py -i " + str(var.get())+" | tee tableau.in")
	subprocess.call("./minetestmapper.py -i " + str(var.get())+" | tee tableau.in" , shell=True)
	subprocess.call("cat tableau.in | ./optimize > dessin.scad" , shell=True)
	subprocess.call("openscad -o "+str(cible.get())+" dessin.scad" , shell=True)

fen1 = Tk()
fen1.title("Convertisseur Minetest vers STL")
frame1 = Frame (fen1,width=600, height=100)
frame1.pack()

var = StringVar()
var.set('Selectionnez votre monde à imprimer')
tex1 = Label(frame1,textvariable =var, fg='black')
tex1.grid(sticky=E,row=2, column=1)
cible = StringVar()
cible.set('Selectionnez le chemin cible')
tex2 = Label(frame1,textvariable =cible, fg='black')
tex2.grid(sticky=E,row=3, column=1)


bou1 = Button(frame1, text='Selectionner le dossier monde', command = Ouvrir)
bou1.grid(sticky=W,row=2, column=0)


bou4 = Button(frame1, text='Selectionner le fichier à enregistrer', command = Enregistrer)
bou4.grid(sticky=W,row=3, column=0)

bou2 = Button(frame1, text='Convertir', command = Convertir)
bou2.grid(sticky=W,row=5, column=0)


bou3 = Button(frame1, text='Quitter', command = fen1.destroy)
bou3.grid(sticky=W,row=5, column=1)

fen1.mainloop()


