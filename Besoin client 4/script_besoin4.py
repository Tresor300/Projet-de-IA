import pandas as pd
import pickle
import time
import sys

def animer_texte(texte):
    """Petite fonction pour faire un effet 'machine à écrire' dans le terminal."""
    for char in texte:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.02)
    print()

def predire_puissance_interactive():
    try:
        # 1. Chargement des modèles
        with open('modele_puissance.pkl', 'rb') as f:
            modele = pickle.load(f)
        with open('encodeur_implantation.pkl', 'rb') as f:
            encodeur = pickle.load(f)

        print("\n" + "="*60)
        animer_texte("⚡ BIENVENUE DANS LE PRÉDICTEUR DE PUISSANCE DE BORNES ⚡")
        print("="*60 + "\n")

        # 2. Interactions avec l'utilisateur
        # On propose les choix reconnus par l'encodeur
        choix_implantations = list(encodeur.classes_)
        print("Types d'implantations disponibles :")
        for i, type_impl in enumerate(choix_implantations):
            print(f"  [{i+1}] {type_impl}")
        
        index_impl = int(input(f"\n Choisissez un type d'implantation (1-{len(choix_implantations)}) : ")) - 1
        implantation = choix_implantations[index_impl]

        nbre_pdc = int(input(" Combien de points de charge prévoyez-vous ? : "))
        latitude = float(input(" Saisissez la Latitude (ex: 48.8566 pour Paris) : "))
        longitude = float(input(" Saisissez la Longitude (ex: 2.3522 pour Paris) : "))

        # 3. Traitement
        print("\n" + "-"*60)
        animer_texte("🤖 L'IA analyse ces informations...")
        time.sleep(1) # Petite pause pour le suspense

        implantation_code = encodeur.transform([implantation])[0]
        
        donnees_borne = pd.DataFrame({
            'implantation_station': [implantation_code],
            'nbre_pdc': [nbre_pdc],
            'consolidated_latitude': [latitude],
            'consolidated_longitude': [longitude]
        })
        
        # 4. Prédiction
        prediction = modele.predict(donnees_borne)
        
        # 5. Affichage du résultat final
        print("="*60)
        animer_texte(f" PUISSANCE NOMINALE RECOMMANDÉE : {prediction[0]} kW 🎯")
        print("="*60 + "\n")
        
    except ValueError:
        print("\n❌ Erreur : Veuillez entrer un nombre valide.")
    except IndexError:
        print("\n❌ Erreur : Ce choix d'implantation n'existe pas.")
    except FileNotFoundError:
        print("\n❌ Erreur : Fichiers '.pkl' introuvables. Exécutez 'generer_modele.py' d'abord.")
    except Exception as e:
         print(f"\n❌ Une erreur inattendue s'est produite : {e}")

# --- POINT D'ENTRÉE ---
if __name__ == "__main__":
    predire_puissance_interactive()