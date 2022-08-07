import random

NOMBRE_MIN = 1
NOMBRE_MAX = 10

# poser les questions à l'utilisateur
def poser_questions():

    nombre1 = random.randint(NOMBRE_MIN, NOMBRE_MAX)
    nombre2 = random.randint(NOMBRE_MIN, NOMBRE_MAX)

    # Résultat de l'addition
    addition = nombre1 + nombre2

    # Demander le résultat de l'addition à l'utilisateur
    resultat = int(input(f"Votre réponse de l'addition {nombre1} + {nombre2} : "))
    
    if resultat == addition:
        return f"votre réponse '{resultat}' est correct"
    else: 
        return f"votre réponse '{resultat}' est incorrect"

print(f" ^^^: {poser_questions()}")
        
