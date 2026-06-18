import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
import folium
from folium.plugins import HeatMap
import os
import sys
import time

def animer_texte(texte, vitesse=0.02):
    """Petite fonction pour faire un effet 'machine à écrire' dans le terminal."""
    for char in texte:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(vitesse)
    print()

def creer_les_cartes_interactives():
    print("\n" + "="*60)
    animer_texte("🗺️  GÉNÉRATION DES CARTES GPS (CLUSTERING) 🗺️")
    print("="*60 + "\n")

    # 1. Demander le fichier à l'utilisateur
    fichier_donnees = input("👉 Entrez le nom de votre fichier de données (Appuyez sur Entrée pour 'export_IA.csv') : ").strip()
    if not fichier_donnees:
        fichier_donnees = "export_IA.csv"

    # Boucle anti-plantage : tant que le fichier n'est pas trouvé, on redemande
    while not os.path.exists(fichier_donnees):
        print(f"\n❌ Erreur : Le fichier '{fichier_donnees}' est introuvable.")
        print(f"💡 Info : Le terminal cherche actuellement dans ce dossier : {os.getcwd()}")
        choix = input("👉 Tapez le bon nom de fichier (ou 'q' pour quitter) : ").strip()
        if choix.lower() == 'q':
            print("Arrêt du script.")
            return
        fichier_donnees = choix

    # 2. Demander le nombre de clusters (Interactivité)
    k_input = input("\n👉 Combien de zones (clusters) voulez-vous identifier ? (Appuyez sur Entrée pour 6) : ").strip()
    n_clusters = int(k_input) if k_input.isdigit() else 6

    # 3. Chargement des données
    print("\n" + "-"*60)
    animer_texte(f"[1/4] Chargement des données depuis '{fichier_donnees}'...")
    df = pd.read_csv(fichier_donnees, low_memory=False)
    df = df.dropna(subset=['consolidated_latitude', 'consolidated_longitude'])
    
    # 4. L'Intelligence Artificielle (K-Means)
    animer_texte(f"[2/4] Entraînement de l'IA K-Means pour trouver {n_clusters} zones...")
    coordonnees = df[['consolidated_latitude', 'consolidated_longitude']]
    
    scaler = StandardScaler()
    coordonnees_scalees = scaler.fit_transform(coordonnees)
    
    kmeans = KMeans(n_clusters=n_clusters, random_state=42, n_init=10)
    df['Cluster'] = kmeans.fit_predict(coordonnees_scalees)

    # 5. Création de la Carte de Chaleur
    animer_texte("[3/4] Création de la carte de chaleur (Densité)...")
    carte_chaleur = folium.Map(location=[46.603354, 1.888334], zoom_start=6)
    donnees_chaleur = df[['consolidated_latitude', 'consolidated_longitude']].values.tolist()
    HeatMap(donnees_chaleur, radius=10, blur=15).add_to(carte_chaleur)
    carte_chaleur.save('carte_chaleur.html')

    # 6. Création de la Carte des Clusters
    animer_texte("[4/4] Création de la carte des zones stratégiques...")
    carte_clusters = folium.Map(location=[46.603354, 1.888334], zoom_start=6)
    
    # Liste de couleurs étendue pour Folium (au cas où l'utilisateur demande beaucoup de zones)
    couleurs_base = ['red', 'blue', 'green', 'purple', 'orange', 'darkred', 'lightred', 'beige', 'darkblue', 'darkgreen', 'cadetblue', 'darkpurple', 'white', 'pink', 'lightblue', 'lightgreen', 'gray', 'black', 'lightgray']
    couleurs = (couleurs_base * (n_clusters // len(couleurs_base) + 1))[:n_clusters]
    
    # Échantillon pour éviter de faire ramer le navigateur web
    echantillon = df.sample(n=min(3000, len(df)), random_state=42)
    
    for _, ligne in echantillon.iterrows():
        folium.CircleMarker(
            location=[ligne['consolidated_latitude'], ligne['consolidated_longitude']],
            radius=3,
            color=couleurs[ligne['Cluster']],
            fill=True,
            fill_opacity=0.7
        ).add_to(carte_clusters)
        
    carte_clusters.save('carte_clusters.html')

    print("\n" + "="*60)
    animer_texte("✅ OPÉRATION TERMINÉE AVEC SUCCÈS ! ✅")
    print("Deux fichiers ont été créés dans votre dossier :")
    print("  1. 'carte_chaleur.html'")
    print("  2. 'carte_clusters.html'")
    print("Ouvrez-les dans votre navigateur Web (Chrome, Edge, Safari...)")
    print("="*60 + "\n")

# --- POINT D'ENTRÉE ---
if __name__ == "__main__":
    creer_les_cartes_interactives()