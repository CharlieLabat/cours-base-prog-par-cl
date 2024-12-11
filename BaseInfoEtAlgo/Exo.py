# Je vous donne une phrase 
# Et vous demande de 
# compter le nombre de A dans la phrase

p1 = "Tout code pour un ordi est traduit en binaire, les mots-clés et caractères sont des codes binaires traduits pour nous"
nb=0
phrase=list(p1)
print(phrase)
for i in phrase:
    if i=="a":
        nb=nb+1
print("il y a " + str(nb) + " 'a' dans la phrase")

# Creer une fonction qui si le nombre est pair
# diviser par 2 sinon tripler eux et ajouter 1

def view(n):
    if(n%2==0):
        return(n/2)
    else:
        return(n*3+1)
print(view(1000))      