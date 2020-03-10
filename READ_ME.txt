
*** Comment est structuré ce répertoire ? ***

Sous la racine se trouve :

- Le code utilisé pour la modélisation, sous forme de Notebook "code_modelisation"
- Un Notebook "résultats" pour l'analyse des résultats 
- Un script "demo", qui permet d'effectuer des prédiction sur des images

Le dossier 'demo_data' contient les données nécessaires à l'utilisation du script de démonstration.

Le dossier résultats contient les historiques des modélisations effectuées, ainsi que les modèles retenus.



*** Comment utiliser ce répertoire ? ***

Pour l'utilisation du script de démonstration (les librairies nécessaires doivent être installées) :

	- Placer la ou les images à tester dans le dossier 'images' du répertoire 'demo_data' 
	  (images couleur au format jpg uniquement)

	- Lancer le script 'demo' sous la racine

	- indiquer le nom de l'image sur laquelle effectuer la prédiction (par exemple 'pampa')

	- cliquer sur le bouton 'Prédire la race'

Le programme affichera ensuite l'image du chien, indiquera sa race ainsi que sa probabilité d'appartenance à celle ci.
A noter que le lancement peut pendre un peu de temps car le modèle se charge ainsi que les librairies.

Pour le lancement du script le plus simple est de créer un fichier batch qui le lance automatiquement.
Exemple générique de lancement via l'Anaconda prompt :

CALL 'emplacement du script d'activation d'environnement' 'emplacement de l'environnement'
cd 'emplacement du script à lancer'
python 'nom du script'



*** Quelles sont les librairies nécessaires ? ***

version de python :  3.6.9

Les versions suivantes ont été utilisées :

- Keras 2.24
- Tensorflow 2.0
- pillow 6.2.1
- Numpy 1.17.4
- Pandas 0.25.3
- scikit-learn 0.22.1 (uniquement pour les résultats)
- seaborn 0.9.0
- matplolib 3.1.1

