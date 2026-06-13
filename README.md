# Puissance 4 Graphique


Une implémentation graphique du célèbre jeu **Puissance 4** développée en Python. Ce projet utilise la bibliothèque graphique `graphics_nsi`, fournit par mon professeur de NSI, pour offrir une interface visuelle interactive où les joueurs cliquent directement sur le plateau pour placer leurs jetons.

---

## 🎮 Fonctionnalités du Jeu

* **Interface Graphique Active :** Une fenêtre de 700x600 pixels affiche une grille de jeu traditionnelle (6 lignes et 7 colonnes).
* **Contrôles à la Souris :** Les joueurs jouent au clic. Le script détecte automatiquement dans quelle colonne le joueur a cliqué pour y empiler un jeton.
* **Astuce Algorithmique de Victoire :** Pour détecter l'alignement de 4 jetons (horizontal, vertical ou diagonal), le code utilise une logique arithmétique astucieuse :
  * Un jeton **Rouge** vaut `1`. Une somme de `4` sur un axe déclenche la victoire rouge.
  * Un jeton **Jaune** vaut `50`. Une somme de `200` sur un axe déclenche la victoire jaune.
* **Effets Visuels de Fin :** Lorsqu'un joueur gagne, toute la grille flash aux couleurs du vainqueur (totalement rouge ou totalement jaune) !

---

## 🛠️ Structure du Code

Le projet est structuré autour de plusieurs fonctions clés :
* `grille()`, `grilleRouge()`, `grilleJaune()` : Gestion de l'affichage et des animations colorées du damier.
* `dessineJeton(P, couleur)` : Calcule la gravité, place le cercle coloré au bon endroit et met à jour la matrice du plateau.
* `victoire()` : Vérifie de manière exhaustive les combinaisons gagnantes en exploitant les valeurs numériques attribuées aux jetons.
* `Tour()` : Gère l'alternance des joueurs au clic et détecte la situation de match nul.

---

## 🚀 Comment lancer le jeu ?

### Prérequis
* Avoir Python 3 installé.
* Disposer du module `graphics_nsi.py` dans le même dossier que le script du jeu.

### Exécution
Ouvrez votre terminal dans le dossier contenant le projet et lancez :
```bash
python3 puissance_4.py
```
