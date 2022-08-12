import random
from tkinter import N

NOMBRE_MIN = 1
NOMBRE_MAX = 10
NOMBRE_QUESTIONS = 4
nb_points = 0
# poser les questions à l'utilisateur
def poser_questions():

    nombre1 = random.randint(NOMBRE_MIN, NOMBRE_MAX)
    nombre2 = random.randint(NOMBRE_MIN, NOMBRE_MAX)
    op = random.randint(0 , 1)  # le 0 représente +, le 1 représente le *
    
    if op == 0:

        # Si c'est l'addition
        operateur_str = "+"
        # Résultat de l'addition
        calcul = nombre1 + nombre2
    else:
        # C'est la multiplication
        operateur_str = "*"
        calcul = nombre1 * nombre2

     # Demander le résultat de l'addition à l'utilisateur
    resultat = int(input(f"Votre réponse de l'opération {nombre1} {operateur_str} {nombre2} : "))
    
    if resultat == calcul:
        return True
   
    return False

nb_points = 0
for i in range(NOMBRE_QUESTIONS):
    print(f"Question {i + 1} / {NOMBRE_QUESTIONS}")
    
    if poser_questions(): # return true
        nb_points += 1
        print("réponse correcte")
    else:
        print("réponse incorrecte")

print(f"Vous avez {nb_points} points / {NOMBRE_QUESTIONS} !!")

if nb_points == NOMBRE_QUESTIONS:
    print("Bravo vous êtes excellent !!!")
elif nb_points == 0:
    print("Vous devez réviser vos cours ....")

moyenne = round(NOMBRE_QUESTIONS / 2)

if nb_points > moyenne:
    print("Pas mal, vous êtes supérieur à la moyenne..")
elif nb_points < moyenne:
    print("^^ peut mieux faire ^^")
else:
    print("Vous êtes dans la moyenne..")

   
