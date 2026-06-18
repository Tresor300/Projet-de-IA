Projet IA - Besoin Client 1 : Analyse Exploratoire et Nettoyage des Données
Auteur: Trésor

📌 Description du Projet

Ce dossier contient la solution technique répondant au "Besoin 1" du cahier des charges : réaliser l'Analyse Exploratoire des Données (EDA), traiter les valeurs aberrantes ou manquantes, et consolider les données brutes des bornes de recharge pour véhicules électriques.

L'objectif de cette étape fondatrice est de transformer un jeu de données brut en un fichier fiable et structuré (export_IA.csv), qui servira de socle sain pour tous les algorithmes d'Intelligence Artificielle développés dans les besoins suivants (Clustering, Classification, etc.).

📂 Structure du Dossier

donnees_brutes.csv : Le jeu de données initial et non traité, tel que fourni par le client.

BesoinClient1.ipynb : Le Jupyter Notebook détaillant toute la démarche (Exploration, visualisation des distributions, nettoyage, traitement des valeurs nulles, et feature engineering).

export_IA.csv : Le livrable final de cette phase. C'est le jeu de données propre, exporté automatiquement à la fin du Notebook.

⚙️ Prérequis et Installation

Assurez-vous d'utiliser un environnement Python (idéalement 3.9+) avec les bibliothèques d'analyse et de visualisation installées :

pip install pandas numpy matplotlib seaborn


🚀 Comment utiliser ce projet ?

Phase d'Analyse et de Nettoyage (Notebook)

Pour comprendre la méthodologie d'analyse ou reproduire le nettoyage des données :

Ouvrez BesoinClient1.ipynb dans VS Code ou Jupyter.

Exécutez les cellules de haut en bas pour visualiser les graphiques d'analyse de la qualité des données.

La toute dernière cellule se chargera de générer et sauvegarder le fichier export_IA.csv sur votre disque dur.

📊 Synthèse des Résultats

Traitement des doublons : Identification et suppression des stations enregistrées en double.

Valeurs manquantes : Imputation ou suppression stratégique des lignes présentant des données GPS (Latitude/Longitude) ou des puissances nominales manquantes.

Valeurs aberrantes (Outliers) : Correction ou exclusion des erreurs de saisie détectées lors de l'analyse (ex: puissances négatives, coordonnées hors de la France métropolitaine).

Livrable : Un dataset consolidé, standardisé et prêt pour le Machine Learning, garantissant l'absence de "bruit" technique pour l'entraînement des futurs modèles.