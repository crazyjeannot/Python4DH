# Import des modules nécessaires
import re  # Module pour les expressions régulières
from collections import Counter  # Objet de comptage

# Fonction pour découper le texte en mots
def decouper_en_mots(un_morceau_de_texte):
    texte_minuscule = un_morceau_de_texte.lower()  # Convertir en minuscules
    mots_separes = re.split("\W+", texte_minuscule)  # Séparer les mots
    return mots_separes  # Retourner la liste de mots

# Chemin d'accès du texte
chemin_du_texte = "../data/1907_Leblanc-Maurice_Arsene-Lupin-gentleman-cambrioleur.txt"

# Nombre de mots les plus fréquents à afficher
nombre_de_mots_voulu = 40

# Liste des mots vides à exclure
mots_vides = [
    # ... (liste complète des mots vides)
]

# Lire le texte complet depuis le fichier
texte_complet = open(chemin_du_texte, encoding="utf-8").read()

# Découper le texte en mots
tous_les_mots = decouper_en_mots(texte_complet)

# Filtrer les mots significatifs en enlevant les mots vides
mots_significatifs = [mot for mot in tous_les_mots if mot not in mots_vides]

# Compter le nombre d'occurrences de chaque mot significatif
conteur_mots_significatifs = Counter(mots_significatifs)

# Extraire les mots les plus fréquents
mots_significatifs_frequents = conteur_mots_significatifs.most_common(nombre_de_mots_voulu)

# Afficher les mots les plus fréquents
print("Les", nombre_de_mots_voulu, "mots les plus fréquents sont :")
print(mots_significatifs_frequents)