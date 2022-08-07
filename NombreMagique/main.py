import random

# Nombre magique entre 1 Et 10
NOMBRE_MIN = 1
NOMBRE_MAX = 10
NOMBRE_VIES = 4  # Nombre de fois essayées

# On crée une variable de vie pour tester dessus
vies = NOMBRE_VIES

# nombre d'essais
tentatives = 0

# Nombre magique aléatoire
NOMBRE_MAGIQUE = random.randint(NOMBRE_MIN , NOMBRE_MAX)

def demander_nombre(nb_min, nb_max):
    # demander un nombre entre (1 et 10)
    nombre_ret = 0

    # Si la nombre saisie n'est pas valide on reboucle
    while nombre_ret == 0:
        try:
            nombre_ret = int(
                input(f"Quel est le nombre magique entre {nb_min} et {nb_max}: "))
           
        except ValueError:
            print("Le nombre est non valide, veuillez resaisir !!")
        else:
            if nombre_ret < nb_min or nombre_ret > nb_max:
                print(f"Le nombre n'est pas entre {nb_min}, et {nb_max} veuillez resaisir...")

                # on met à zéro pour reboucler  ===> Saisie non valide
                nombre_ret = 0
    return nombre_ret

nombre = 0
# retour du nombre saisie

# nombre de vies


while nombre != NOMBRE_MAGIQUE and vies > 0:
    # le nombre magique est plus grand
    nombre = demander_nombre(NOMBRE_MIN, NOMBRE_MAX)

    if nombre > NOMBRE_MAGIQUE:
        print("nombre magique est plus grand")
        vies -= 1
        tentatives += 1
        print(f"Il vous reste {vies} vie(s)")

    # le nombre magique est plus petit
    elif nombre < NOMBRE_MAGIQUE:
        print("nombre magique est plus petit")
        vies -= 1
        tentatives += 1
        print(f"Il vous reste {vies} vie(s)")
    
# On test le cas ou on a pas de vies  ===> vies = 0, on a perdu
if vies == 0:

    print(f"Vous avez perdu, le nombre magique est : {NOMBRE_MAGIQUE}, vous n'avez pas de vies !!!")
else:
    # Vous avez gagné, avec un nombre de vie > 0
    print(f"Bravo vous avez gagné après {tentatives} tentatives, et avec {vies} vies")
