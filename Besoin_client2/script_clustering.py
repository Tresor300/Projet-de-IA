"""

script_clustering.py
====================
Besoin Client 2 — Clustering selon la position géographique

Usage :
    python script_clustering.py --latitude 48.8566 --longitude 2.3522
    python script_clustering.py --latitude 43.2965 --longitude 5.3698 --info

Description :
    Prend en entrée les coordonnées GPS d'une borne de recharge et renvoie
    le numéro du cluster auquel elle appartient, en chargeant le modèle
    K-Means préalablement entraîné. Aucun réentraînement n'est effectué.

Prérequis :
    modeles/kmeans_clustering.pkl
    modeles/scaler_clustering.pkl
    modeles/meta_clustering.json

    
"""

import argparse
import sys
import os
import json
import numpy as np
import warnings
warnings.filterwarnings('ignore')

try:
    import joblib
except ImportError:
    print("Package 'joblib' manquant. Installez-le : pip install joblib")
    sys.exit(1)

BASE_DIR      = os.path.dirname(os.path.abspath(__file__))
MODELE_KMEANS = os.path.join(BASE_DIR, "modeles", "kmeans_clustering.pkl")
MODELE_SCALER = os.path.join(BASE_DIR, "modeles", "scaler_clustering.pkl")
META_FILE     = os.path.join(BASE_DIR, "modeles", "meta_clustering.json")


def verifier_fichiers():
    for chemin in [MODELE_KMEANS, MODELE_SCALER]:
        if not os.path.exists(chemin):
            print(f"Fichier manquant : {chemin}")
            print("Exécutez d'abord le notebook d'entraînement.")
            sys.exit(1)


def charger_modele():
    return joblib.load(MODELE_KMEANS), joblib.load(MODELE_SCALER)


def charger_meta():
    if os.path.exists(META_FILE):
        with open(META_FILE, "r") as f:
            return json.load(f)
    return {}


def predire_cluster(latitude: float, longitude: float) -> int:
    """Prédit le cluster d'une borne à partir de ses coordonnées GPS."""
    verifier_fichiers()
    kmeans, scaler = charger_modele()

    if not (41.0 <= latitude <= 51.5):
        print(f"Avertissement : latitude {latitude} hors plage France métropolitaine.")
    if not (-5.5 <= longitude <= 10.0):
        print(f"Avertissement : longitude {longitude} hors plage France métropolitaine.")

    # Normalisation identique à l'entraînement
    coords = np.array([[latitude, longitude]])
    coords_df = __import__('pandas').DataFrame(
        coords, columns=['latitude', 'longitude']
    )
    coords_scaled = scaler.transform(coords_df)
    return int(kmeans.predict(coords_scaled)[0])


def main():
    parser = argparse.ArgumentParser(
        description="Prédit le cluster géographique d'une borne IRVE."
    )
    parser.add_argument("--latitude",  type=float,
                        help="Latitude de la borne (ex: 48.8566)")
    parser.add_argument("--longitude", type=float,
                        help="Longitude de la borne (ex: 2.3522)")
    parser.add_argument("--info", action="store_true",
                        help="Affiche les informations du modèle")

    # parse_known_args ne lève pas d'exception SystemExit si les arguments manquent
    args, unknown = parser.parse_known_args()

    # Si on clique sur "Play", latitude et longitude vaudront None. 
    # On leur donne alors des valeurs par défaut (Paris).
    if args.latitude is None or args.longitude is None:
        print("\n[Avis] Aucun argument détecté dans le terminal.")
        print("-> Exécution automatique avec les coordonnées par défaut (Paris).\n")
        args.latitude = 48.8566
        args.longitude = 2.3522
        args.info = True  # On force l'affichage des métriques pour la démo

    if args.info:
        meta = charger_meta()
        if meta:
            print("\nInformations sur le modèle :")
            print(f"  k (clusters)       : {meta.get('k_optimal')}")
            print(f"   Silhouette Coefficient  : {meta.get('silhouette')}")
            print(f"  Calinski-Harabasz  : {meta.get('calinski_harabasz')}")
            print(f"  Davies-Bouldin     : {meta.get('davies_bouldin')}")
            print(f"  Bornes (train)     : {meta.get('n_bornes')}\n")

    print(f"Coordonnées : lat={args.latitude}, lon={args.longitude}")
    cluster = predire_cluster(args.latitude, args.longitude)
    print(f"Cluster associé : {cluster}")
    return cluster

    if args.info:
        meta = charger_meta()
        if meta:
            print("\nInformations sur le modèle :")
            print(f"  k (clusters)       : {meta.get('k_optimal')}")
            print(f"  Silhouette Score   : {meta.get('silhouette')}")
            print(f"  Calinski-Harabasz  : {meta.get('calinski_harabasz')}")
            print(f"  Davies-Bouldin     : {meta.get('davies_bouldin')}")
            print(f"  Bornes (train)     : {meta.get('n_bornes')}\n")

    print(f"Coordonnées : lat={args.latitude}, lon={args.longitude}")
    cluster = predire_cluster(args.latitude, args.longitude)
    print(f"Cluster associé : {cluster}")
    return cluster


if __name__ == "__main__":
    main()


