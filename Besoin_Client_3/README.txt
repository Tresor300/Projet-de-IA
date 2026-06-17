Auteur : Ozias Groupe 7

Projet IA - Besoin Client 3

Description :
Ce projet a pour objectif de résoudre le besoin client 3 en utilisant un modèle de Machine Learning.

Contenu du dossier :
- data.csv : base de données utilisée
- notebook.ipynb : analyse et entraînement du modèle
- script_final.py : version finale du code
- modele.pkl : modèle entraîné sauvegardé

Instructions :
1. Ouvrir le notebook pour voir l’analyse
2. Lancer le script_final.py pour utiliser le modèle

Script de prédiction du type d’implantation

Objectif : Ce script permet de predire le type d'implantation en fonction de plusieurs paramètres comme le type de prise, le type de paiement, le nombre de port de charge, la puissance nominale, l'accessibilité et autres. 

Etape 1: Avant d’exécuter le script, vérifier que les fichiers suivants sont présents dans le même dossier : modele_random_forest.pkl; encoders.pkl; encoder_y.pkl
Etape 2: Puis lancer le script dans le terminal "python script.py"
Etape 3: Le script va vous demander de saisir différentes informations sur une borne de recharge. Entrer 1=0 pour Vrai et pour tout autre valeur que 1 est Faux. 

Exemple d'execution

Nombre de points de charge : 2
Puissance nominale (kW) : 50
Prise Type 2 (1=VRAI / 0=FAUX) : 1
Prise Combo CCS (1=VRAI / 0=FAUX) : 1
Prise CHAdeMO (1=VRAI / 0=FAUX) : 0
Paiement à l'acte (1=VRAI / 0=FAUX) : 1
Condition d'accès (1=Accès libre, 0=Accès restreint) : 1
Réservation (1=VRAI / 0=FAUX) : 0
Accessibilité PMR (1=Accessible / 0=Non accessible) : 1
Restriction de gabarit (1=Aucune / 0=Hauteur max 3m) : 1
Horaires (1=24h/24 / 0=horaires limités) : 1

Resultats obtenus:

Type d'implantation prédit :  "Parking privé à usage public"

Prédiction terminée