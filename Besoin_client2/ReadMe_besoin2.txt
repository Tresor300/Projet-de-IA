================================================================================
README - Besoin Client 2 : Clustering selon la position

================================================================================

DESCRIPTION
-----------
Ce script effectue un clustering géographique des bornes de recharge (IRVE)
selon leur position (latitude/longitude). Il charge un modèle de clustering
préalablement enregistré et retourne le cluster associé à une borne donnée.

IMPORTANT : Le script ne relance PAS l'entraînement à chaque exécution.
Il charge le modèle (.pkl) préalablement sauvegardé.


CONTENU DU DOSSIER
------------------
  - export_IA.csv         : Base de données utilisée (issue de la partie Big Data)
  - clustering.ipynb      : Notebook expérimental commenté (entraînement, métriques,
                            visualisation)
  - predict_cluster.py    : Script final en ligne de commande
  - clustering_model.pkl  : Modèle de clustering enregistré
  - README.txt            : Ce fichier


UTILISATION DU SCRIPT FINAL
-----------------------------
Le script prend en entrée la latitude et la longitude d'une borne de recharge
et retourne le numéro de cluster associé.


MÉTRIQUES UTILISÉES POUR ÉVALUER LE CLUSTERING
------------------------------------------------
  - Silhouette Coefficient  : mesure la cohésion et la séparation des clusters
                              (valeur entre -1 et 1, plus proche de 1 = meilleur)
  - Calinski-Harabasz Index : ratio dispersion inter/intra cluster
                              (plus la valeur est élevée = meilleur)
  - Davies-Bouldin Index    : moyenne des similarités entre clusters
                              (plus la valeur est faible = meilleur)


ALGORITHME UTILISÉ
-------------------
  Voir le notebook clustering.ipynb pour le détail du choix de l'algorithme,
  la détermination du nombre optimal de clusters et la discussion des résultats.
  Référence : https://scikit-learn.org/stable/modules/clustering.html


VISUALISATION
--------------
  La carte interactive des clusters est générée dans le notebook (.ipynb).
  Chaque cluster est représenté par une couleur différente sur la carte.


REMARQUES
----------
  - Le modèle doit être entraîné une première fois via le notebook avant
    d'utiliser le script.
  - Ne pas modifier le fichier clustering_model.pkl.
  - Le script échouera si le fichier .pkl est absent du répertoire.

================================================================================