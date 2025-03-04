import tkinter as tk
from tkinter import messagebox
from random import randint

#---------------------------------------------------------------CLASSE DE L'ARBRE------------------------------------------------------------

class ArbreBinaireRecherche:
    def __init__(self, val):
        self.valeur = val
        self.sag = None  # Sous-arbre gauche
        self.sad = None  # Sous-arbre droit
 
    def __str__(self):
        """Permet d'afficher la valeur de la racine de l'arbre"""
        return str(self.valeur)
    
    def ajoute(self, cle):
        """Ajoute une clé à l'arbre binaire de recherche"""
        if cle < self.valeur:
            if self.sag is None:
                self.sag = ArbreBinaireRecherche(cle)
            else:
                self.sag.ajoute(cle)
        elif cle > self.valeur:
            if self.sad is None:
                self.sad = ArbreBinaireRecherche(cle)
            else:
                self.sad.ajoute(cle)

    def taille(self):
        """Permet de renvoyer la taille de l'arbre"""
        if self.sag is None:
            tSAG = 0
        else:
            tSAG = self.sag.taille()
        if self.sad is None:
            tSAD = 0
        else:
            tSAD = self.sad.taille()
        return 1 + tSAG + tSAD

    def hauteur(self):
        """Permet de renvoyer la hauteur de l'arbre"""
        if self.sag is None:
            hSAG = -1
        else:
            hSAG = self.sag.hauteur()
        if self.sad is None:
            hSAD = -1
        else:
            hSAD = self.sad.hauteur()
        return 1 + max(hSAG, hSAD)

    def afficheArbre(self, profondeur=0):
        """Permet l'affichage de l'arbre dans la console avec un décalage des noeuds proportionnel à la profondeur du noeud.
        L'affichage de l'arbre est horizontal (Droite en haut et Gauche en bas)"""
        if self.sad:
            self.sad.afficheArbre(profondeur + 1)
        print(f"{profondeur * 6 * ' '}{self.valeur}")
        if self.sag:
            self.sag.afficheArbre(profondeur + 1)

#------------------------------------------------------------CLASSE DE L'APPLICATION---------------------------------------------------------

class Application:
        
    def __init__(self):
        # Création du canevas
        fenetre = tk.Tk()
        fenetre.title("Arbre Binaire de Recherche")
        self.canevas = tk.Canvas(fenetre, width=1500, height=700)
        self.canevas.create_line(1000, 0, 1000, 700)
        self.canevas.create_line(1000, 450, 1500, 450)
        self.canevas.pack()
        
        # Création des widgets
        self.labelInc = tk.Label(fenetre, text="propriété de Vauchel Inc®, ne pas copier sous peine d'emprisonnement")
        self.labelTaille = tk.Label(fenetre, fg="red", text="Taille :")
        self.labelTailleVar = tk.Label(fenetre, text=" ")
        self.labelHauteur = tk.Label(fenetre, fg="green", text="Hauteur :")
        self.labelHauteurVar = tk.Label(fenetre, text=" ")
        self.labelBoutons = tk.Label(fenetre, text="Zone des boutons utilitaires")
        self.labelArbre = tk.Label(fenetre, text="Zone du schéma de l'arbre")
        self.labelCles = tk.Label(fenetre, text="Zone de saisie des clés")
        self.labelRacine = tk.Label(fenetre, text="Entrez la racine voulue ici :")
        self.labelPositionCles = tk.Label(fenetre, text="Entrez les valeurs des clés ci-dessous :")
        self.labelTailleVar = tk.Label(fenetre, text=' ')
        self.labelEffacement = tk.Label(fenetre, fg="red", text=' ')

        self.boutonDessiner = tk.Button(fenetre, text="Dessiner l'arbre", fg="green", command=self.recupererValeurs)
        self.boutonRéinitialiser = tk.Button(fenetre, text="Réinitialiser l'arbre", fg="gray", command=self.reinitialiser)
        self.boutonAPropos = tk.Button(fenetre, text="A propos", fg="blue", command=self.aPropos)
        self.boutonQuitter = tk.Button(fenetre, text="Quitter le programme", command=fenetre.destroy)
        self.boutonExemple = tk.Button(fenetre, text ="Créer un exemple", fg="purple", command = self.exemple)
        
        self.entréeRacine = tk.Entry(fenetre, width=5)
        
        # Positions des widgets
        self.boutonDessiner.place(x=1120, y=550)
        self.boutonRéinitialiser.place(x=1050, y=600)
        self.boutonAPropos.place(x=1250, y=550)
        self.boutonQuitter.place(x=1300, y=600)
        self.boutonExemple.place(x = 1175, y = 600)
        
        self.labelInc.place(x=1120, y=685)
        self.labelHauteur.place(x=1150, y=425)
        self.labelHauteurVar.place(x=1210, y=425)
        self.labelTaille.place(x=1050, y=425)
        self.labelTailleVar.place(x=1090, y=425)
        self.labelCles.place(x=1175, y=25)
        self.labelArbre.place(x=400, y=25)
        self.labelBoutons.place(x=1185, y=470)
        self.labelRacine.place(x=1075, y=75)
        self.labelPositionCles.place(x=1075, y=125)
        self.labelEffacement.place(x=0, y=685)
        
        self.entréeRacine.place(x=1220, y=75)
        
        #Crée les entrées graçe à une boucle
        self.listeNomsEntrées = []
        for i in range(2, 32):
            NomEntrée = f"entrée{i}"
            entrée = tk.Entry(fenetre, width=5)
            entrée.place(x=1075 + ((i - 2) % 6) * 50, y=175 + ((i - 2) // 6) * 30)
            self.listeNomsEntrées.append(NomEntrée)
            setattr(self, NomEntrée, entrée)

        #Fin du programme
        fenetre.mainloop()
        print("Programme terminé")

    def reinitialiser(self):
        """Permet de réinitialiser totalement l'entièreté des variables pour construire un nouvel arbre"""
        #Efface les valeurs dans les entrées
        self.entréeRacine.delete(0, tk.END)
        for NomEntrée in self.listeNomsEntrées:
            getattr(self, NomEntrée).delete(0, tk.END)

        #Réinitialise la liste de valeurs
        self.valeurs = [''] * 15
        
        #Efface la phrase d'information si hauteur > 4
        self.labelEffacement.config(text=" ")
        
        #Efface le contenu du canevas
        self.canevas.delete("all")
        
        
        #Redessine les lignes qui délimitent les trois parties effacées initialement
        self.canevas.create_line(1000, 0, 1000, 700)
        self.canevas.create_line(1000, 450, 1500, 450)
        
    def aPropos(self):
        """Permet d'ouvrir une fenêtre Pop Up qui expliquera comment utiliser l'application"""
        #Création d'un nouveau canevas pour afficher les informations
        porte = tk.Tk()
        porte.title("Comment marche l'application ?")
        canevapa = tk.Canvas(porte, width=660, height=200)
        canevapa.pack()
        
        #Les informations
        tk.Label(porte, fg="green", text="Cliquer sur le bouton Dessiner permet aux valeurs saisies d'apparaître dans l'arbre.").place(x=0, y=0)
        tk.Label(porte, fg="gray", text="Cliquer sur le bouton Réinitialiser effacera toutes les valeurs saisies ainsi que l'arbre.").place(x=0, y=20)
        tk.Label(porte, text="Cliquer sur le bouton Quitter permet de fermer l'application.").place(x=0, y=40)
        tk.Label(porte, fg="purple", text="Cliquer sur le bouton Exemple fera apparaître un arbre avec des valeurs aléatoires.").place(x=0, y=60)
        tk.Label(porte, fg="lightblue", text="Vous devez saisirs les valeurs à mettre dans l'arbre binaire de recherche.").place(x=0, y=80)
        tk.Label(porte, fg="red", text="ATTENTION : La hauteur maximal de l'arbre est de 4, les valeurs qui font passer la hauteur au dessus de 4 seront supprimées.").place(x=0, y=100)
        tk.Label(porte, fg="red", text="ATTENTION : Les valeurs entrées ne doivent pas être inférieures à 1 ou supérieures à 99, et ce sont forcément des entiers.").place(x=0, y=120)
        tk.Label(porte, fg="red", text="ATTENTION : Si vous rentrez deux fois la même valeur, elle n'apparaîtra qu'une seule fois.").place(x=0, y=140)
        tk.Label(porte, fg="red", text="REMARQUE : Si vous n'avez pas saisi de racine, la première valeur rentrée deviendra la racine.").place(x=0, y=160)
        tk.Label(porte, fg="blue", text="INFORMATION : Modifier une valeur saisie modifiera l'arbre en remplaçant l'ancienne valeur par la nouvelle entrée.").place(x=0, y=180)

    def recupererValeurs(self):
        """Récupère les valeurs entrées et vérifie si ce sont bien des entiers compris entre 1 et 99 et qu'il n'y a pas de doublons"""
        self.listeValeurs = [self.entréeRacine.get()] + [getattr(self, NomEntrée).get() for NomEntrée in self.listeNomsEntrées]

        valeursInt = set()  #On utilise un ensemble pour vérifier les doublons

        for v in self.listeValeurs:
            if v:  #Si v existe (la valeur est autre chose que '')
                if not isinstance(v, (int, str)):
                    tk.messagebox.showerror("Erreur", "Les valeurs doivent uniquement être des entiers (réinitialisez pour recommencer).")
                    raise ValueError("Erreur", "Les valeurs doivent uniquement être des entiers (réinitialisez pour recommencer).")

                try:
                    valeurInt = int(v)
                except ValueError:  #Si la valeur entrée est autre chose qu'un nombre entier, renvoyer une erreur
                    tk.messagebox.showerror("Erreur", "Les valeurs doivent uniquement être des entiers (réinitialisez pour recommencer).")
                    raise ValueError("Erreur", "Les valeurs doivent uniquement être des entiers (réinitialisez pour recommencer).")
                    return

                if not (1 <= valeurInt <= 999):  #Si la valeur n'est pas comprise entre 1 et 99, renvoyer une erreur
                    tk.messagebox.showerror("Erreur", "Les valeurs doivent être des entiers entre 1 et 99 (réinitialisez pour recommencer).")
                    raise ValueError("Erreur", "La valeur doit être un entier entre 1 et 99 (réinitialisez pour recommencer).")
                    return


                valeursInt.add(valeurInt)  #Ajouter la valeur à l'ensemble
        
        self.creationArbre()  #Si il n'y a aucune erreur, on commence à créer l'arbre

    def creationArbre(self):
        """Crée l'arbre avec les valeurs correctement saisies, vérifie si la liste n'est pas vide et que la hauteur maximale n'est pas dépassée
        et met à jour l'arbre si une valeur est remplacée par une autre"""
        
        #Efface la phrase d'information si hauteur > 4
        self.labelEffacement.config(text=" ")
        
        valeursInt = [int(v) if v else None for v in self.listeValeurs]  #Convertit en int seulement si la valeur n'est pas vide
        valeursInt = list(filter(None, valeursInt))  #Supprime les valeurs None

        if valeursInt == []:  #Si la liste est vide, renvoyer une erreur
            tk.messagebox.showerror("Erreur", "Veuillez entrer au moins une valeur pour construire un arbre.")
            raise ValueError("Erreur:", "Veuillez entrer au moins une valeur pour construire un arbre.")

        #Crée un arbre avec les valeurs actuelles/nouvelles
        AB1 = ArbreBinaireRecherche(valeursInt[0])
        for valeur in valeursInt[1:]:
            AB1.ajoute(valeur)

        self.taille = AB1.taille()
        self.labelTailleVar.config(text=self.taille)  #Renvoie la taille
        self.hauteur = AB1.hauteur()
        self.labelHauteurVar.config(text=self.hauteur)  #Renvoie la hauteur

        #Si la hauteur dépasse 4, supprime les valeurs et ajuste l'arbre
        if self.hauteur > 4:
            self.labelEffacement.config(text = "ATTENTION : Des valeurs ont été supprimées pour limiter la hauteur à 4 !")
            while self.hauteur > 4:
                valeursInt.pop()  #Supprime la dernière valeur
                AB1 = ArbreBinaireRecherche(valeursInt[0])
                for valeur in valeursInt[1:]:
                    AB1.ajoute(valeur)
                self.hauteur = AB1.hauteur()
                self.labelHauteurVar.config(text=self.hauteur)

        #Efface le contenu du canevas
        self.canevas.delete("all")

        #Redessine les lignes qui délimitent les trois parties effacées initialement
        self.canevas.create_line(1000, 0, 1000, 700)
        self.canevas.create_line(1000, 450, 1500, 450)

        self.dessinerArbre(AB1, 450, 150, 3)


    def dessinerArbre(self, arbre, x, y, niveau, largeur=700, espacementHorizontal=200, espaceVertical=100):
        """Dessine l'arbre sur le canevas avec les valeurs entrées triées pour créer un arbre binaire de recherche"""
        rayon = 20  #Rayon du cercle représentant un nœud

        if arbre:
            #Dessiner le nœud
            self.canevas.create_oval(x - rayon, y - rayon, x + rayon, y + rayon, fill="lightblue")
            self.canevas.create_text(x, y, text=str(arbre.valeur))

            #Dessiner la branche gauche
            if arbre.sag:
                xGauche = x - espacementHorizontal
                yGauche = y + espaceVertical
                self.canevas.create_line(x - 15, y + rayon - 7, xGauche, yGauche - rayon, width=2, fill="black")
                self.dessinerArbre(arbre.sag, xGauche, yGauche, niveau - 1, largeur / 2, espacementHorizontal / 2)

            #Dessiner la branche droite
            if arbre.sad:
                xDroite = x + espacementHorizontal
                yDroite = y + espaceVertical
                self.canevas.create_line(x + 15, y + rayon - 7, xDroite, yDroite - rayon, width=2, fill="black")
                self.dessinerArbre(arbre.sad, xDroite, yDroite, niveau - 1, largeur / 2, espacementHorizontal / 2)

    def exemple(self):
        """Crée un arbre avec des valeurs aléatoires"""
        self.listeValeurs = [randint(1, 999) for i in range(randint(6, 10))]
        self.creationArbre()

#Crée une instance de l'application
application = Application()

