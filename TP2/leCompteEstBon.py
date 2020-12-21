#!/usr/bin/python
#Auteur Valynseele Alexis
#Licence 3 Informatique

import random
from typing import Iterable

#Pour créer tout les couples
def permutations(iterable, r=None):
    # permutations('ABCD', 2) --> AB AC AD BA BC BD CA CB CD DA DB DC
    # permutations(range(3)) --> 012 021 102 120 201 210
    pool = tuple(iterable)
    n = len(pool)
    r = n if r is None else r
    if r > n:
        return
    indices = list(range(n))
    cycles = list(range(n, n-r, -1))
    yield tuple(pool[i] for i in indices[:r])
    while n:
        for i in reversed(range(r)):
            cycles[i] -= 1
            if cycles[i] == 0:
                indices[i:] = indices[i+1:] + indices[i:i+1]
                cycles[i] = n - i
            else:
                j = cycles[i]
                indices[i], indices[-j] = indices[-j], indices[i]
                yield tuple(pool[i] for i in indices[:r])
                break
        else:
            return

def tirage():
    valeurs = [1,1,2,2,3,3,4,4,5,5,6,6,7,7,8,8,9,9,10,10,25,25,50,50,75,75,100,100]
    pn = []
    cible = random.randint(100,999)

    for i in range(0,6):
        pn.append(valeurs[random.randint(0,(len(valeurs) - 1 ))])

    return pn,cible

#Question 1 : construire tout les couples (pi,pj) de Pn
def constructionCouples(pn:Iterable):
    return permutations(pn,2)

def quatreEnsemble(couple):
    resultat = []
    resultat.append(couple[0] + couple[1])
    resultat.append(couple[0] * couple[1])
    if couple[0] - couple[1] >= 0:
        resultat.append(couple[0] - couple[1])
    if(couple[1]!=0):
        if couple[0] % couple[1] == 0:
            resultat.append(int(couple[0] / couple[1]))
    return resultat

def constructionQuatreEnsembles(couples:Iterable):
    resultat = []
    for i in couples:
        resultat.append(quatreEnsemble(i))
    return resultat



def constructionSousEtat(Pn,pn1,cible):
    incr=0
    excess=0
    for i in range(0,len(pn1)):
        if(i!=0 and (i%(len(Pn)-1))==0):
            incr+=1
            excess=0
        if(i%len(Pn)==0):
            excess+=1
        elemDel1 = Pn[incr]
        elemDel2 = Pn[(i%(len(Pn)-1))+excess]

        for j in range(0,len(pn1[i])):
            result = Pn.copy()
            result.remove(elemDel1)
            result.remove(elemDel2)
            result.append(pn1[i][j])

            constructionSousEnsemble(result.copy(),cible)




def constructionSousEnsemble(Pn,cible):
    if(len(Pn)==1 and Pn[0]==cible):
        print(Pn)
    else:
        couples = constructionCouples(Pn)
        pn_1 = constructionQuatreEnsembles(couples)
        constructionSousEtat(Pn,pn_1,cible)

# Handling argv and running main      
if __name__ == "__main__":
    pn,cible = tirage()
    couples = constructionCouples(pn)
    couples = list(couples) #On obtient une liste de tuples (les couples de permutations)
    print("pn = "+str(pn))
    print("cible = "+str(cible))
    pn_1 = constructionQuatreEnsembles(couples)
    print("\n\n\n")
    constructionSousEtat(pn,pn_1,cible)
    print("test")