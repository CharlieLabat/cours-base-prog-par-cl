
# String : Les phrases qu'on utilise au quotidien
# Toujours avec des guillemets (") et parfois avec des cotes (')
# Char : un caractère ! Java par exemple considère que string est une classe et char le type primaire
print("Bonjour je suis une chaîne de caractère ou String composée de caractère ou char")
# Les nombres sont dans beaucoup de langage divisé en deux types, les entiers et les décimaux
# 
# Integer : Les nombres sans partie décimale comme 2 ou -3
print (1)
print ("Est un nombre, un entier ou int plus précisément ")
# Float/Double : Les nombres avec partie décimal comme 2.25 ou pi (les nombres irrationnels sont arrondi )
print (3.14)
print ("Est un nombre, une décimale ou float/double plus précisément ")
# Boolean : Vrai ou Faux ou en anglais True ou False.
# Notez que ces mots-clé ne sont pas utilisés dans tout les langages
print ("false et true sont des booléens, des mots clés qui expriment le résultat d'une condition")
# Collection : Ensemble de variable (ou d'objet/d'instance). Il existe plus forme de collections
# Liste : Collection d'élément de n'importe quel type, indexée automatiquement par des clés numérique 
# Attention : toute liste ou collection commence dans la plupart des langages par 0 
# C'est le premier nombre !

chiffre = [0,1,2,3,4,5,6,7,8,9]

for i in chiffre:
    print(str(i)+ " est un élément de la liste")

print(str(len(chiffre))+" est le total d'élément")