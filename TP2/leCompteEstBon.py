#!/usr/bin/python
#Auteur Valynseele Alexis
#Licence 3 Informatique

import random
from typing import Iterable
from timeit import default_timer as timer

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

#Question 1 : construire tous les couples (pi,pj) de Pn
def constructionCouples(pn:Iterable):
    return permutations(pn,2)

#Contruit tous les résultats des combinaisons d'opérations possibles pour un couple
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
#met les résultats obtenus precedant  pour tous les couples dans un tableau
def constructionQuatreEnsembles(couples:Iterable):
    resultat = []
    for i in couples:
        resultat.append(quatreEnsemble(i))
    return resultat


#Construit les nouveaux ensemble avec l'ajout des résultats des differentes opérations tout en enlevant le couple ayant permis ce resultat
def constructionEnsemble(Pn,pn1,cible,tabOperation):
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
            tabOperation.append([elemDel1,elemDel2,j])
            constructionSousEnsemble(result.copy(),cible,tabOperation)
            tabOperation.remove([elemDel1,elemDel2,j])




def constructionSousEnsemble(Pn,cible,tabOperation):
    if(len(Pn)==1 and Pn[0]==cible):
        print(Pn)
        print(tabOperation)
        end = timer()
        print(end-start)
        exit()
    else:
        couples = constructionCouples(Pn)
        pn_1 = constructionQuatreEnsembles(couples)
        constructionEnsemble(Pn,pn_1,cible,tabOperation)

     
def exploration(pn,cible):
    tabOperation=[]
    
    couples = constructionCouples(pn)
    couples = list(couples) #On obtient une liste de tuples (les couples de permutations)
    
    pn_1 = constructionQuatreEnsembles(couples)
    constructionEnsemble(pn,pn_1,cible,tabOperation)

start = timer()
def main():
    pn,cible = tirage()
    print("pn = "+str(pn))
    print("cible = "+str(cible)+"\n")
    exploration(pn,cible)
    print("parcouru sans rien trouve")
    end = timer()
    print(end-start)
    return 


main()