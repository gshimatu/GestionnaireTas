# GestionnaireTas 
Un travail d'algorithme pour la gestion des tas min et max

Question : Faites un programme python qui demande à l’utilisateur de rajouter les valeurs d’une liste tas max et tas min . Notez que l’arbre binaire doit être complet avec une jonction qui organise les données 

Pour le faire je me suis donc dit de réaliser une sorte de gestionnaire des Tas binaire 

Déjà il faut savoir si c'est quoi un Tas binaire ? 🤔
Un tas binaire (ou "binary heap" en anglais) est une structure de données spécialisée qui prend la forme d'un arbre binaire complet. Il est principalement utilisé pour implémenter des files de priorité. 

Mais c'est quoi maintenant un arbre binaire complet ? 🤔
C'est tout simplement un arbre dont tous les niveaux de ce dernier sont complètement remplis, sauf peut-être le dernier niveau, qui est rempli de gauche à droite.

Un Tas peut être tas min ou tas max 
- Tas min : Pour chaque nœud, la valeur du nœud est inférieure ou égale aux valeurs de ses enfants. La racine contient la plus petite valeur.
- Tas max : Pour chaque nœud, la valeur du nœud est supérieure ou égale aux valeurs de ses enfants. La racine contient la plus grande valeur.

Structure de mon code 👨‍💻

Le programme utilise la bibliothèque standard heapq de Python pour gérer efficacement les tas min et max.

1. Ménu principal
   L'utilisateur peut choisir parmi trois options : ajouter une valeur, afficher les tas ou quitter le programme.
   
2. Ajout des valeurs
   La valeur est ajoutée à la fois dans le tas min et le tas max.
   Pour le tas max, les valeurs sont stockées en négatif pour inverser l'ordre naturel du tas min, ce qui simule un tas max.

3. Affichage des tas
   Le tas min est affiché tel quel
   Le tas max est affiché avec les valeurs restaurées (multiplication par -1)

4. Complétude de l'arbre
  Les tas min et max sont représentés sous forme de liste dans heapq, qui garantit automatiquement une organisation conforme.

By Gauthier Shimatu 👨‍💻
