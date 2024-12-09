# Un classique pour montrer comment marche l'informatique : Salut le monde
print("Hello World")
# Varions ce Hello World 
def hello(mot) :
    return("Hello " + mot)
# Reprenons notre exemple dans la diapo (Algo de parité)
def parite(n) : 
    if (n%2==0): # On cherche si N à comme reste 0 quand on le divise par 2 (Modulo)
        return str(n) + " est un nombre pair"
    else:
        return str(n) + " est un nombre impair"
# Exemple de variable
gem = "GEM"
# Allons voir nos résultats 
print(hello(gem))
print(hello("My Friend"))
print(parite(3))
print(parite(4))
