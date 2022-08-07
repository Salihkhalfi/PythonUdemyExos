print("Hello SalihosCode")
name = "Saliha"
age = 25
une_liste = ["Salih", "Kadour", "Amar", 1, 2, 3545]
is_adult = age >= 18
# --------------------------------------------------------------------------------------------
if is_adult:
    print("Hello " + name + " Tu as " + str(age) +
          " ans " + "Majeure est : " + str(is_adult))
else:
    """
        * is_adult change en false automatiquement en False si age < 18
        * Pas la peine de mettre "not is_adult"
        * Jouer avec la variable age est vous verrez exple: age = 15
    """
    print("Hello " + name + " Tu as " + str(age) +
          " ans " + "Majeure est : " + str(is_adult))

# -----------------------------------------------------------------------------------------
print("Tu as les oives suivants avec : " + str(une_liste))
print(name.upper())
other_name = name.replace("S", "m").upper()

# Entoure "MALIHA par des * =====> **MALIHA**
# le premier chiffre représente le nbre total des * plus MALIHA (* + other_name)
print(other_name.center(10, "*"))
print("La longueur de other_name = 'MELIHA' est égal à : " + str(len(other_name)))
# -----------------------------------------------------------------------------------------
print("est ce que 'LIHA' est dans other_name ? " + str("LIHA" in other_name))
# -----------------------------------------------------------------------------------------
commentaire = """
Salut les copains
    Salut les loulous
        brefs c'est le Ramadhan
"""
print("le commentaire multiligne est égal à :")
print(commentaire)
# -----------------------------------------------------------------------------------------
# -----------Les F Strings ----------------------------------------------------------------
name = "Salih"
age = 56
email = f"""
        Hello {name} how are you?
        you are {age} years old.
        """
print("Ton message de mail : ")
print(email)
# -----------------------------------------------------------------------------------------
# -------------------------------LES COMPARAISONS  ----------------------------------------
print(14 >= 11)
print((14 != 11) and (10 <= 4) and ("A" == "a"))
print(not ((14 != 11) and (10 <= 4) and ("A" == "a")))
# -----------------------------------------------------------------------------------------
# -------LES AFFECTATIONS -----------------------------------------------------------------
brand = "Amigoscode"
print(brand)
# -----------------------------------------------------------------------------------------
# ------------------------------FLOW CONTROL ----------------------------------------------
# number = int(input("Donner votre variable à evaluer :"))
# if number > 0:
#     print(f"la variable number = {number} est positive.")
# elif number == 0:
#     print(f"la variable number = {number} est nulle")
# else:
#     print(f"la variable number = {number} est négative")
# # ------------------------------Autre Méthode térnaire ------------------------------------
# number = int(input("Donner votre variable à evaluer :"))
# message = "Positive" if number > 0 else "0 ou négative"
# print(f"la variable number est:  {message}")

# # ----------------------------LES LISTES ---------------------------------------------------
liste = [14, 7, 31, 0, -12, 63, -10]
liste.sort()
print(liste.sort())  # ======> Retourne None, il faut faire un print sur "liste"
print(f"La liste triée est : {liste}")
print(f"La liste triée à l'envers est : {liste.reverse()}")

liste.append(1000)
print(f"La liste avec 1000 ajouté est :{liste}")
print(liste.sort())  # ======> Retourne None, il faut faire un print sur "liste"
print(f"La liste triée est : {liste}")
print(f"La longueur de la liste est: {len(liste)}")

# Rajoute des elts à liste impérativement entre crochets []
liste.extend([20, 21, 30])
print(f"La liste étendue est : {liste}")

liste.remove(1000)
print(f"La liste sans 1000 est : {liste}")
del liste[2]  # Supprime un elt de la liste à l'index liste[n]
print(f"la liste sans le troisème elt est : {liste}")
# Suprime les deux premiers elts ======> [-12, -10, 7, 14, 31, 63, 20, 21, 30]
del liste[0: 2]
# ======================================================> [7, 14, 31, 63, 20, 21, 30]
print(f"La liste sans les 2 premiers elts : {liste}")

print(liste)
variable = liste.pop()  # pop() suprime le dernier elt de la liste
print(f"la liste sans la dernière valeur {variable} est : {liste}")
print(f"La liste sans 1000 est : {liste}")

liste.clear()  # efface toute la liste
print(f"La liste est vide : {liste}")

liste = [-12, -10, 0, 7, 14, 31, 63, 20, 21, 30, 1000]
message = "vrai" if 35 in liste else "faux"  # ======> Condition ternaire
print(f"est ce que 25 est dans la liste ? : {message}")

# -------------------------Les SETS ------------------------------------------------------------
number_set = {1, 1, 2, 3, 7, 0}
# Ne permet pas la duplication des elts ====> {0, 1, 2, 3, 7}
print(f"Le set est égal à : {number_set}")

lettersA = {"A", "B", "C", "F", "K", "X"}
lettersB = {"K", "B", "E", "T", "Y"}

# =======> {'T', 'E', 'K', 'X', 'Y', 'A', 'C', 'F', 'B'}
union = lettersA | lettersB
# Dans le désordre, l'ordre n'est pas garantie
print(f"L'union égal à : {union}")
intersection = lettersA & lettersB  # =====> {'B', 'K'}
# Dans le désordre, l'ordre n'est pas garantie
print(f"L'intersection égal à : {intersection}")
difference = lettersA - lettersB  # ======> {'C', 'F', 'A', 'X'}
# Dans le désordre, l'ordre n'est pas garantie
print(f"La différence est égal à : {difference}")

# ------------------------LES DICTIONNAIRES --------------------------------------------------------
personne = {
    "nom": "Salih",
    "age": 56,
    "adresse": "Veneux les sablons"
}
print(f"la personne est : {personne}")
age = personne["age"]
print(f"L'age de la personne est : {age}")

print(f"Les clés de ce dictionnaires : {personne.keys()}")  # Les clés du dict
# ====> [Salih', 56, 'Veneux les sablons']
print(f"Les Valeurs de ce dictionnaires : {personne.values()}")

# ====> ['nom', 'age', 'adresse'] , donne que la liste des clés mais pas les Valeurs
list_personne = list(personne)
print(f"Transformation dict ==> liste : {list_personne}")

items = personne.items()  # Donne une liste de tuple ===> (key , value) du dictionnaires
# ========================> [('nom', 'Salih'), ('age', 56), ('adresse', 'Veneux les sablons')]
# personne.clear() ===> supprime le dictionnaire

personne["age"] = 100
print(f"la liste aprés changement d'age est  : {personne}")
# donne l'age d'une autre manière  <====> age_changed = personne["age"]
age_changed = personne.get("age")
print(f"la liste aprés changement d'age est  : {age_changed}")

liste = [1, 3, 3, 10, 15, 17, 17, 20, 21]
liste_to_set = list(set(liste))
print(liste_to_set)


# def multiple(n):
#     sum = 0
#     for i in range(1, n):
#         if i % 3 or i % 5 or i % 7:
#             sum += i
#     return sum


# nombre = int(input("Entrer le nombre : "))
# print(f"La somme des multiples de {nombre} est : {multiple(nombre)}")


def is_bool(n1, n2):
    if n1 + n2 == 1:
        return True
    elif n1 == 1 or n2 == 1:
        return True
    else:
        return False


nombre1 = int(input("Nombre 1 : "))
nombre2 = int(input("Nombre 2 : "))

print(f"{nombre1} et {nombre2} renvoient : {is_bool(nombre1, nombre2)}")


