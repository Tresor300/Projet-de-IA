PROJET IA : OPTIMISATION DES BORNES DE RECHARGE EN FRANCE

DESCRIPTION

Projet d'Intelligence Artificielle visant à nettoyer, analyser et exploiter les données des bornes de recharge pour véhicules électriques en France via 4 besoins clients distincts.

STRUCTURE DU PROJET ET OBJECTIFS

Besoin_Client_1 (Analyse et Nettoyage / EDA)

Objectif : Préparer les données pour les algorithmes.

Actions : Suppression des doublons, imputation des valeurs manquantes, exclusion des valeurs aberrantes (GPS hors France, puissances négatives).

Livrable final : Fichier de données propre "export_IA.csv".

Besoin_Client_2 (Regroupement Géographique / Clustering)

Objectif : Identifier les zones de concentration des bornes.

Actions : Entraînement de l'algorithme K-Means sur Latitude/Longitude. Identification de 6 clusters optimaux.

Livrable final : Cartes interactives (.html) et modèle "kmeans_model.pkl".

Besoin_Client_3 (Visualisation / Business Intelligence)

Objectif : Rendre les données lisibles.

Actions : Création de tableaux de bord et de graphiques (KPIs du réseau).

Besoin_Client_4 (Prédiction de Puissance / Classification)

Objectif : Deviner la puissance nominale d'une borne selon son emplacement et son infrastructure.

Actions : Entraînement et optimisation d'un Random Forest via GridSearchCV.

Livrable final : Modèle "modele_puissance.pkl" et script autonome "script_besoin4.py".

INSTALLATION ET PREREQUIS

Langage : Python 3.9+

Bibliothèques requises : pandas, numpy, scikit-learn, matplotlib, seaborn, folium, joblib

Commande d'installation :
pip install pandas numpy scikit-learn matplotlib seaborn folium joblib

GUIDE D'EXECUTION (Ordre chronologique obligatoire)

ETAPE 1 : Exécuter le Notebook du Besoin 1 pour générer le fichier "export_IA.csv".
ETAPE 2 : Exécuter le Notebook du Besoin 2 pour créer les cartes géographiques.
ETAPE 3 : Exécuter le Notebook du Besoin 4 pour entraîner l'IA prédictive.
ETAPE 4 : Tester l'IA finale dans le terminal en exécutant la commande :
python script_besoin4.py