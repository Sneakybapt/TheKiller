#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from tkinter import *
import random
import numpy as np
import pandas as pd
from PIL import ImageTk, Image

class TheKiller(Frame):
    
    def __init__(self, decor, **kwargs):
        Frame.__init__(self, decor, **kwargs)
        #decor.geometry("600x200")
        decor.title("The Killer")
        self.pack(fill=BOTH)
        
        self.fondecran = ImageTk.PhotoImage(Image.open("C:/Users/baptiste/Pictures/TheKiller.jpg"))
        self.w, self.h = self.fondecran.width(), self.fondecran.height()
        self.c = Canvas(decor, width=self.w, height=self.h)
        self.c.create_image((self.w//2, self.h//2), image = self.fondecran)
        decor.geometry("{}x{}".format(self.w, self.h))
        
        self.bouton_recommencer = Button(self.c, text = 'Recommencer', command = self.recommencer, fg = 'red', width = 14, height = 1 )
        self.bouton_recommencer.place(bordermode=INSIDE)
        
        self.player = StringVar()
        self.Nom_joueur = Entry(self.c, textvariable = self.player,  )
        
        self.bouton_jouer = Button(self.c, text = 'Jouer', command = self.jouer, width = 10, height = 1)
        
        self.bouton_creer = Button(self.c, text = 'Création du jeu', command = self.creer)
        
        self.bouton_ajouter = Button(self.c, text = 'Ajouter un nouveau joueur', command = self.ajouter_joueur)
        
        self.bouton_cacher = Button(self.c, text = 'Cacher', command = self.cacher)
        
        self.message_cible = Label(self.c, text = "Cible :", fg = 'red', )
        
        self.message_mission = Label(self.c, text = "Mission :", fg = 'red')
        
        self.message_pret = Label(self.c, text = 'Jeu pas pret', fg = 'red')
        
        self.message_encouragement = Label(self.c, text = "Loading...", fg = 'blue', font = ('italic', '10'))
        
        self.longueur_liste = 0
        self.liste_joueur = Listbox(self.c, height = self.longueur_liste, width = 12, )
        
        self.nb_joueur = 0
        
        self.c.create_window(510,70, window = self.bouton_cacher)
        self.c.create_window(510,35, window = self.bouton_jouer)
        self.c.create_window(510,365, window = self.bouton_recommencer)
        self.c.create_window(70,365, window = self.bouton_creer)
        self.c.create_window(100, 35, window = self.bouton_ajouter)
        self.c.create_window(self.w//2, 35, window = self.Nom_joueur)
        self.c.create_window(self.w//2, 365, window = self.message_pret)

        self.c.pack()
        
        self.participants = []
        self.cible = []
        
    def creer(self):
        
        self.c.create_window(300,150, window = self.message_mission)
        self.c.create_window(300,100, window = self.message_cible)
            
        self.file = pd.read_csv("C:/Users/baptiste/Documents/Jeu Pyhton/Defis.txt", sep = ",")
        self.missions = self.file.Test

        self.players = []
        self.targets = []
        random.shuffle(self.participants)
        
        for i in range(0, len(self.participants)-1):
            self.players += [self.participants[i]]
            self.targets += [self.participants[i+1]]
        self.players += [self.participants[len(self.participants)-1]]
        self.targets += [self.participants[0]]
        
        self.message_pret["text"] =  "Jeu prêt !"
        self.message_pret["fg"] = "green"
        
        self.c.create_window(self.w//2, 250, window = self.message_encouragement)
        
    
    def jouer(self):
        if self.player.get() != '':
            self.index = self.players.index(self.player.get())
            self.num_mission = random.randint(0,len(self.missions)-1)
            self.mission_a_faire = self.missions[self.num_mission]
            self.missions.truncate(self.mission_a_faire)
            self.cible = self.targets[self.index]
            self.message_cible["text"] = "Cible : {}".format(self.cible)
            self.message_mission["text"] = "Mission : {}".format(self.mission_a_faire)
        else  :
            self.message_cible["text"] = 'Réapuye sur jouer'
            self.message_mission["text"] = 'Réapuye sur jouer'
        
        self.message_encouragement["text"] = "Puisse le sort vous être favorable"
        
    
    def ajouter_joueur(self):
        
        self.liste_joueur.insert(END, self.player.get())
        self.c.create_window(70, 190, window = self.liste_joueur)
        self.nb_joueur += 1
        self.longueur_liste += 1
        self.participants += [self.player.get()]
        self.Nom_joueur.delete(0, len(self.player.get()))
        
        
    def recommencer(self):
        
        self.participants = []
        self.cible = []
        
        self.players = []
        self.targets = []
        
        self.message_cible["text"] = "Cible :"
        self.message_mission["text"] = "Mission : "
        
        self.message_pret["text"] =  "Jeu pas prêt"
        self.message_pret["fg"] = "red"
        
        while self.liste_joueur.size() != 0:
            
            for i in range(0,self.liste_joueur.size()):
                
                self.liste_joueur.delete(i)
        self.Nom_joueur.delete(0, len(self.player.get()))
    
    def cacher(self):
        
        self.message_cible["text"] = "Cible :"
        self.message_mission["text"] = "Mission : "
        self.Nom_joueur.delete(0, len(self.player.get()))
        
        self.message_encouragement["text"] = "Loading..."

fenetre = Tk()
interface = TheKiller(fenetre,)
interface.mainloop()


# In[ ]:




