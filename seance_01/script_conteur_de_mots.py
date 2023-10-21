# Import des modules nécessaires
import re  # Module pour les expressions régulières
from collections import Counter  # Objet de comptage

# Fonction pour découper le texte en mots
def decouper_en_mots(un_morceau_de_texte):
    texte_minuscule = un_morceau_de_texte.lower()  # Convertir en minuscules
    mots_separes = re.split("\W+", texte_minuscule)  # Séparer les mots
    return mots_separes  # Retourner la liste de mots

# Chemin d'accès du texte
chemin_du_texte = "../data/txt/1907_Leblanc-Maurice_Arsene-Lupin-gentleman-cambrioleur.txt"

# Nombre de mots les plus fréquents à afficher
nombre_de_mots_voulu = 40

# Liste des mots vides à exclure
mots_vides = ['je', 'tu', 'il', 'elle', 'on', 'nous', 'vous', 'ils', 'elles',
    'le', 'la', 'les', 'un', 'une', 'des', 'mon', 'ma', 'mes', 'ton', 'ta', 'tes',
    'son', 'sa', 'ses', 'notre', 'votre', 'leurs', 'de', 'du', 'l', 'à', 'au', 'aux', 'en', 'par', 'pour', 'avec',
    'sur', 'sous', 'dans', 'vers', 'contre', 'à travers', 'après', 'avant', 'pendant',
    'alors', 'quand', 'si', 'comme', 'parce que', 'parce', 'mais', 'ou', 'et', 'donc',
    'si', 'car', 'lorsque', 'puisque', 'qu', 'quel', 'quelle', 'quels', 'quelles',
    'ainsi', 'autant', 'autre', 'autres', 'celui', 'celle', 'ceux', 'celles',
    'chaque', 'ci', 'ça', 'cela', 'ce', 'ceci', 'celui-ci', 'celle-ci',
    'celui-là', 'celle-là', 'cent', 'certain', 'certaine', 'certaines', 'certains',
    'ceux-ci', 'ceux-là', 'chaque', 'combien', 'comme', 'd', 'dans', 'des', 'du', 'deux',
    'devant', 'donc', 'dont', 'duquel', 'elle', 'elles', 'en', 'encore', 'entre',
    'envers', 'est', 'et', 'eu', 'eux', 'fin', 'fut', 'hormis', 'hui', 'huit', 'ici',
    'il', 'ils', 'je', 'jusque', 'l', 'la', 'le', 'les', 'leur', 'leurs', 'lors',
    'lui', 'là', 'ma', 'mais', 'me', 'même', 'mes', 'moi', 'moins', 'mon', 'ne', 'ni',
    'nombreuses', 'nombreux', 'notre', 'nous', 'ou', 'où', 'par', 'parmi', 'pas',
    'peu', 'plus', 'plupart', 'pour', 'pourquoi', 'quand', 'que', 'quel', 'quelle',
    'quelles', 'quels', 'qui', 'quoi', 'sa', 'sans', 'se', 'sept', 'ses', 'si',
    'sien', 'soi', 'soit', 'son', 'sont', 'sous', 'soyez', 'sujet', 'sur', 'ta',
    'tandis', 'te', 'tel', 'telle', 'telles', 'tels', 'tes', 'toi', 'ton', 'tous',
    'tout', 'toute', 'toutes', 'un', 'une', 'va', 'vers', 'voici', 'voilà', 'vont',
    'votre', 'vous', 'vu', 'ça', 's', 'n', 'c', 'a', 'm', 'j', 'y', 't', 'ces', 
    'dit', 'cet', 'oui', 'non', 'était', 'est', 'être', 'été', 'ai', 'puis', 'avez', 
    'avait', 'avais', 'eût', 'très', 'cette', 'point', 'fois', 'fit', 'aussi', 'suis' 
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