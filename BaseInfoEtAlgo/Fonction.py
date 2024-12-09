# Une fonction
# Bout de code réutilisable avec un ou des entrées et un ou des sorties
def f(x):
    return "Ceci est une fonction de forme : " + x
print(f("2x+3"))

# Une procédure
# Fonction sans entrée qui gère des traitements cachés 
def phraseALaNoix():
    return("Python est un langage très facile à comprendre et à utiliser")
print(phraseALaNoix())

# Element d'un algo 

# Condition (if/else)
# Si une proposition est vrai alors elle donne un résultat sinon un autre
# if signifie "si", else "sinon" et rarement then signifie "alors"
def posOuNeg(n):
    if(n>0) :
        return str(n) + " est positif"
    elif(n<0) :
        return str(n) + " est négatif"
    else:
        return str(n) + " est nul"

print(posOuNeg(5))
print(posOuNeg(-5))
print(posOuNeg(0))


