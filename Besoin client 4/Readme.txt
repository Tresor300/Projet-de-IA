Projet IA - Besoin Client 4 : Prédiction de la Puissance Nominale
développeur ##Trésor

📌 Description du Projet

Ce dossier contient la solution technique répondant au "Besoin 4" du cahier des charges : développer une Intelligence Artificielle capable de prédire automatiquement la puissance nominale (en kW) d'une borne de recharge pour véhicules électriques en fonction de ses caractéristiques (localisation GPS, type d'implantation, nombre de points de charge).

L'approche choisie est un modèle d'Apprentissage Supervisé (Classification) utilisant l'algorithme Random Forest, optimisé via GridSearchCV.

📂 Structure du Dossier

export_IA.csv : Le jeu de données initial (nettoyé) utilisé pour l'entraînement.

BesoinClient4.ipynb : Le Jupyter Notebook détaillant toute la démarche (Feature Engineering, Entraînement, Évaluation, Matrices de confusion).

script_besoin4.py : Le script Python autonome (Livrable final) permettant de faire des prédictions instantanées.

modele_puissance.pkl : Fichier généré automatiquement (Le "cerveau" de l'IA sauvegardé).

encodeur_implantation.pkl : Fichier généré automatiquement (L'encodeur pour transformer le texte en données numériques).

⚙️ Prérequis et Installation

Assurez-vous d'utiliser un environnement Python (idéalement 3.9+) avec les bibliothèques suivantes installées :

pip install pandas scikit-learn matplotlib seaborn


🚀 Comment utiliser ce projet ?

1. Phase d'Entraînement (Notebook)

Pour comprendre la méthodologie, générer les graphiques d'évaluation ou ré-entraîner le modèle :

Ouvrez BesoinClient4.ipynb dans VS Code ou Jupyter.

Exécutez toutes les cellules de haut en bas.

À la fin de l'exécution, les fichiers .pkl seront mis à jour sur votre disque.

2. Phase de Production (Script autonome)

Pour tester l'IA en conditions réelles, sans relancer l'entraînement :

Ouvrez un terminal dans le dossier Besoin_Client_4.

Exécutez la commande suivante :

python script_besoin4.py


Le script affichera la puissance prédite pour la borne configurée dans le code.

📊 Synthèse des Performances

Modèle : Random Forest Classifier

Optimisation : Validation croisée avec GridSearchCV.

Variables prédictives (Importance) : Position GPS (Latitude/Longitude, ~63%), Type d'implantation (~20%), Nombre de points de charge (~16%).

Précision globale (Accuracy) : ~52%.

Note : Ce score s'explique par la présence de nombreuses valeurs cibles ultra-minoritaires et aberrantes (ex: 22.08 kW, 104 kW). Le modèle repère avec succès les standards industriels majeurs (50 kW, 120 kW, 150 kW). Pour une mise en production future, il est recommandé de regrouper les puissances en 3 macro-catégories (Charge Lente, Rapide, Ultra-Rapide) pour dépasser les 85% de précision.