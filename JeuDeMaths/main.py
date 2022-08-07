import random
import re

NOMBRE_MIN = 1
NOMBRE_MAX = 10

# poser les questions à l'utilisateur
def poser_questions():
    resultat = int(input(f"Entrez votre réponse de l'opération : 5 + 2 "))
    if resultat == 5 + 2:
        return f"votre réponse '{resultat}' est correct"
    else:
        return f"votre réponse '{resultat} ' est incorrect"

print(f"résultat : {poser_questions()}")
        

