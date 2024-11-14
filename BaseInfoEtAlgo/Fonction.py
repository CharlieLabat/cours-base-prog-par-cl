# Une fonction
def f(x):
    return "Ceci est une fonction de forme : " + x
print(f("2x+3"))

# Une procédure
def phraseALaNoix():
    return("Python est un langage très facile à comprendre et à utiliser")
print(phraseALaNoix())

# Element d'un algo 

# Condition (if/else)
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


