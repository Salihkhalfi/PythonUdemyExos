# Nombre magqie recherché
NOMBRE_MAGIQUE = 5 

# Nombre magique entre 1 Et 10
NOMBRE_MIN = 1
NOMBRE_MAX = 10

def demander_nombre(nb_min , nb_max):
    # demander un nombre entre (1 et 10)
    nombre_ret = int(input(f"Quel est le nombre magique entre {nb_min} et {nb_max}: "))
    return nombre_ret

nombre = 0
# retour du nombre saisie

while nombre != NOMBRE_MAGIQUE:
    # le nombre magique est plus grand
    nombre = demander_nombre(NOMBRE_MIN, NOMBRE_MAX)

    if nombre > NOMBRE_MAGIQUE:
        print("nombre magique est plus grand")

    # le nombre magique est plus petit

    elif nombre < NOMBRE_MAGIQUE:
        print("nombre magique est plus petit")

    # bravo vous avez gagné
    else:
        print("Bravo vous avez gagné")




