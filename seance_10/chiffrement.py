import numpy as np
import pandas as pd
import argparse
import sys
import re
import unidecode

to_morse = {"a":".-", "b":"-...", "c":"-.-.", "d":"-..", "e":".", "f":"..-.", "g":"--.", "h":"....", 
         "i":"..", "j":".---", "k":"-.-", "l":".-..", "m":"--", "n":"-.", "o":"---", "p":".--.", 
         "q":"--.-", "r":".-.", "s":"...", "t":"-", "u":"..-", "v":"...-", "w":".--", "x":"-..-", 
         "y":"-.--", "z":"--.."}

def preprocessing(txt):
    text_sans_accent = unidecode.unidecode(txt)
    text_minus = text_sans_accent.lower()
    text_clean = re.sub(r'[^a-z ]', '', text_minus)
    return text_clean


def encodage(txt, chemin_ecriture, dico_morse, N=1000):
    resultat = ''
    roman = preprocessing(txt)
    for lettre in roman[:N]:
        if lettre in dico_morse:
            resultat+=dico_morse[lettre]+' '
        else:
            resultat+=' '

    with open(chemin_ecriture, 'w') as file_txt:
        file_txt.write(resultat)

    return resultat

def reverse_dico(dico):
    return {dico[cle]:cle for cle in dico.keys()}

def decodage(chemin_lecture_morse, chemin_ecriture, dico_morse):
    text_decode = ''
    with open(chemin_lecture_morse, 'r') as file_morse:
        fichier_morse = file_morse.read()
        liste_char = fichier_morse.split(' ')

        for char in liste_char:
            if char in dico_morse:
                text_decode+=dico_morse[char]
            else:
                text_decode+=' '
        with open(chemin_ecriture, 'w') as fichier_decode:
            fichier_decode.write(text_decode)

    return text_decode  
    

if __name__ == '__main__':
    
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '-i', '--input', help='path to txt file', type=str,  required=True
    )
    parser.add_argument(
        '-o', '--output', help='path output file', type=str,  required=True
    )
    parser.add_argument(
        '-n', '--N_mots', help='le script prend N mots', type=int, default = 1000
    )
    parser.add_argument(
        '-c', '--chiffrement', help='Valeurs possibles: decodage ou encodage', type=str, required=True
    )

    args = vars(parser.parse_args())
    chemin_to_txt = args["input"]
    N = int(args["N_mots"])
    chiffrement = args["chiffrement"]
    chemin_output = args["output"]

    if chiffrement == 'decodage':
        # faire decodage
        reverse_dico_morse = reverse_dico(to_morse)
        decodage_str = decodage(chemin_to_txt, chemin_output, reverse_dico_morse)
        print('Décodage réalisé avec succés !')
    
    elif chiffrement == 'encodage':
        # faire encodage
        with open(chemin_to_txt, 'r') as file_txt:
            fichier_texte = file_txt.read()
            res = encodage(fichier_texte, chemin_output, to_morse, N)
        print('Encodage réalisé avec succés !')
        
    else:
        #sys.exit("Option d'encodage fausse")
        print("Option d'encodage fausse")
        
    
    
