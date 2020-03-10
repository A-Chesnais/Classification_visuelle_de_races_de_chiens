
*** Comment est structur� ce r�pertoire ? ***

Sous la racine se trouve :

- Le code utilis� pour la mod�lisation, sous forme de Notebook "code_modelisation"
- Un Notebook "r�sultats" pour l'analyse des r�sultats 
- Un script "demo", qui permet d'effectuer des pr�diction sur des images

Le dossier 'demo_data' contient les donn�es n�cessaires � l'utilisation du script de d�monstration.

Le dossier r�sultats contient les historiques des mod�lisations effectu�es, ainsi que les mod�les retenus.



*** Comment utiliser ce r�pertoire ? ***

Pour l'utilisation du script de d�monstration (les librairies n�cessaires doivent �tre install�es) :

	- Placer la ou les images � tester dans le dossier 'images' du r�pertoire 'demo_data' 
	  (images couleur au format jpg uniquement)

	- Lancer le script 'demo' sous la racine

	- indiquer le nom de l'image sur laquelle effectuer la pr�diction (par exemple 'pampa')

	- cliquer sur le bouton 'Pr�dire la race'

Le programme affichera ensuite l'image du chien, indiquera sa race ainsi que sa probabilit� d'appartenance � celle ci.
A noter que le lancement peut pendre un peu de temps car le mod�le se charge ainsi que les librairies.

Pour le lancement du script le plus simple est de cr�er un fichier batch qui le lance automatiquement.
Exemple g�n�rique de lancement via l'Anaconda prompt :

CALL 'emplacement du script d'activation d'environnement' 'emplacement de l'environnement'
cd 'emplacement du script � lancer'
python 'nom du script'



*** Quelles sont les librairies n�cessaires ? ***

version de python :  3.6.9

Les versions suivantes ont �t� utilis�es :

- Keras 2.24
- Tensorflow 2.0
- pillow 6.2.1
- Numpy 1.17.4
- Pandas 0.25.3
- scikit-learn 0.22.1 (uniquement pour les r�sultats)
- seaborn 0.9.0
- matplolib 3.1.1

