
# =====================================
# script.py
# Prédiction du type d'implantation
# =====================================

import pandas as pd
import joblib
import os


# =====================================
# Vérification des fichiers nécessaires
# =====================================

fichiers = [
    "modele_random_forest.pkl",
    "encoders.pkl",
    "encoder_y.pkl"
]

for fichier in fichiers:
    if not os.path.exists(fichier):
        raise FileNotFoundError(
            f"Le fichier '{fichier}' est introuvable.\n"
            "Lance notebook.ipynb avant d'exécuter ce script."
        )


# =====================================
# Chargement des modèles
# =====================================

model_rf = joblib.load("modele_random_forest.pkl")
encoders = joblib.load("encoders.pkl")
encoder_y = joblib.load("encoder_y.pkl")

print("Modèles chargés avec succès")


# =====================================
# Fonctions de conversion 
# =====================================

def convert_bool(x):
    return "VRAI" if x == "1" else "FAUX"

def convert_acces(x):
    return "Accès libre" if x == "1" else "restreint"

def convert_pmr(x):
    return "Accessible" if x == "1" else "Non accessible"

def convert_gabarit(x):
    return "Aucune" if x == "1" else "hauteur max 3m"

def convert_horaires(x):
    return "24h/24" if x == "1" else "Mo-Sa 08:30-20:00,Su 08:30-12:15"


# =====================================
# Saisie utilisateur 
# =====================================

print("\n===== Saisie des informations de la borne =====")

try:
    nouvelle_donnee = {

        "nbre_pdc": int(input("Nombre de points de charge : ")),

        "puissance_nominale": float(input("Puissance nominale (kW) : ")),

        "prise_type_2": convert_bool(input("Prise Type 2 (1=VRAI / 0=FAUX) : ")),

        "prise_type_combo_ccs": convert_bool(input("Prise Combo CCS (1=VRAI / 0=FAUX) : ")),

        "prise_type_chademo": convert_bool(input("Prise CHAdeMO (1=VRAI / 0=FAUX) : ")),

        "paiement_acte": convert_bool(input("Paiement à l'acte (1=VRAI / 0=FAUX) : ")),

        "condition_acces": convert_acces(input("Condition d'accès (1=Accès libre, 0=Accès restreint) : ")),

        "reservation": convert_bool(input("Réservation (1=VRAI / 0=FAUX) : ")),

        "accessibilite_pmr": convert_pmr(input("Accessibilité PMR (1=Accessible / 0=Non accessible) : ")),

        "restriction_gabarit": convert_gabarit(input("Restriction de gabarit (1=Aucune / 0=Hauteur max 3m) : ")),

        "horaires": convert_horaires(input("Horaires (1=24h/24 / 0=horaires limités) : "))
    }

except Exception as e:
    print("\n Erreur de saisie :", e)
    print(" Vérifie que tu entres bien des nombres (1 ou 0)")
    exit()


# =====================================
# Conversion en DataFrame
# =====================================

X_new = pd.DataFrame([nouvelle_donnee])


# =====================================
# Nettoyage (identique au notebook)
# =====================================

cols_bool = [
    "prise_type_2",
    "prise_type_combo_ccs",
    "prise_type_chademo",
    "paiement_acte",
    "reservation"
]

for col in cols_bool:
    X_new[col] = X_new[col].fillna("FAUX")

X_new = X_new.fillna("inconnu")


# =====================================
# Encodage
# =====================================

for col, encoder in encoders.items():

    X_new[col] = X_new[col].astype(str)

    valeurs_connues = list(encoder.classes_)

    if "inconnu" in valeurs_connues:
        X_new[col] = X_new[col].apply(
            lambda x: x if x in valeurs_connues else "inconnu"
        )
    else:
        X_new[col] = X_new[col].apply(
            lambda x: x if x in valeurs_connues else valeurs_connues[0]
        )

    X_new[col] = encoder.transform(X_new[col])


# =====================================
# Prédiction
# =====================================

prediction = model_rf.predict(X_new)
implantation = encoder_y.inverse_transform(prediction)


# =====================================
# Résultat final
# =====================================

print("\n==========================")
print("TYPE D'IMPLANTATION PRÉDIT")
print("==========================")

print(f" {implantation[0]}")

print("\n Prédiction terminée")