#!/usr/bin/python
#Auteur Valynseele Alexis
#Licence 3 Informatique

import sys
import numpy
import math
import matplotlib
import matplotlib.pyplot as plt
from timeit import default_timer as timer

def suiteRecu(n:int):
    if n == 1:
        return 1
    elif n == 0:
        return 1
    else:
        return suiteRecu(n-1) + suiteRecu(n-2)

def suiteIteratif(n:int):
    memoire = [1,1]
    if n == 1:
        return memoire[1]
    elif n == 0:
        return memoire[0]
    else:
        for i in range(2,n+1):
            memoire.append(memoire[i-1] + memoire[i-2])
        return memoire[n]

def suiteLoga(n:int): 
    F = [[1, 1], 
         [1, 0]] 
    if (n == 0): 
        return 0
    power(F, n - 1) 
          
    return F[0][0] 

#Multiply a 2 by 2 matrix  
def multiply(F, M): 
  
    x = (F[0][0] * M[0][0] + 
         F[0][1] * M[1][0]) 
    y = (F[0][0] * M[0][1] +
         F[0][1] * M[1][1]) 
    z = (F[1][0] * M[0][0] + 
         F[1][1] * M[1][0]) 
    w = (F[1][0] * M[0][1] + 
         F[1][1] * M[1][1]) 
      
    F[0][0] = x 
    F[0][1] = y 
    F[1][0] = z 
    F[1][1] = w 

#Calculate a matrix to the power n
def power(F, n): 
  
    if( n == 0 or n == 1): 
        return; 
    M = [[1, 1], 
         [1, 0]]; 
          
    power(F, n // 2) 
    multiply(F, F) 
          
    if (n % 2 != 0): 
        multiply(F, M) 
    
#Run suiteRecu with timer
def suiteRecuExecution(n:int):
    #starting the timer
    start = timer()
    suiteRecu(int(n))
    end = timer()
    return (end-start)

#Run suiteIteratif with timer
def suiteIteratifExecution(n:int):
    #starting the timer
    start = timer()
    suiteIteratif(int(n))
    end = timer()
    return (end-start)

def suiteLogaExecution(n:int):
    #starting the timer
    start = timer()
    suiteLoga(int(n))
    end = timer()
    return (end-start)

#Run one test and return the results and write them to the disk
#n data,id du test,nb nombre de test,step le step entre chaque n
def testRecu(n:int,id:int,nb:int,step:int):
    n = int(n)
    results = []
    with open(f'suiteRecu_results_n{id}.txt','w') as f:
        print(f'Runtime of the suite program for n going from 0 to {n}\n', file=f)
        start = timer()
        for i in range(0,n+step,step):
            runtime = suiteRecuExecution(i)
            results.append(runtime)
            print(f"n = {i}\tRuntime = {runtime}", file=f)
            #print(f"test n{id}/{nb} : {i} / {n} [OK]")
        end = timer()
        print(f"\n\nTotal runtime of the test session is {(end-start)} seconds", file=f)
        print(f"\nTotal runtime of the test session is {(end-start)} seconds")
        return results

#Run one test and return the results and write them to the disk
#n data,id du test,nb nombre de test,step le step entre chaque n
def testIteratif(n:int,id:int,nb:int,step:int):
    n = int(n)
    results = []
    with open(f'suiteIteratif_results_n{id}.txt','w') as f:
        print(f'Runtime of the suite program for n going from 0 to {n}\n', file=f)
        start = timer()
        for i in range(0,n+step,step):
            runtime = suiteIteratifExecution(i)
            results.append(runtime)
            print(f"n = {i}\tRuntime = {runtime}", file=f)
            #print(f"test n{id}/{nb} : {i} / {n} [OK]")
        end = timer()
        print(f"\n\nTotal runtime of the test session is {(end-start)} seconds", file=f)
        print(f"\nTotal runtime of the test session is {(end-start)} seconds")
        return results

def testLoga(n:int,id:int,nb:int,step:int):
    n = int(n)
    results = []
    with open(f'suiteLoga_results_n{id}.txt','w') as f:
        print(f'Runtime of the suite program for n going from 0 to {n}\n', file=f)
        start = timer()
        for i in range(0,n+step,step):
            runtime = suiteLogaExecution(i)
            results.append(runtime)
            print(f"n = {i}\tRuntime = {runtime}", file=f)
            #print(f"test n{id}/{nb} : {i} / {n} [OK]")
        end = timer()
        print(f"\n\nTotal runtime of the test session is {(end-start)} seconds", file=f)
        print(f"\nTotal runtime of the test session is {(end-start)} seconds")
        return results
     
#Plot the result + a comparaison of the theoric complexity      
def plotting(results1,results2,results3,n:int,nb:int,step:int):
    #Setting up the plot
    fig, (ax1,ax2) = plt.subplots(1,2)
    x1 = range(0,n+step,step)
    #Plotting our results
    for i in range(0,nb):
        #Selectionnez quels tests vous voulez graph
        ax1.plot(x1,results1[i], label=f'test n°{i+1} iteratif')
        #ax1.plot(x1,results2[i], label=f'test n°{i+1} recursif')
        ax1.plot(x1,results3[i], label=f'test n°{i+1} logarithmique')
    ax1.set(xlabel=f'n with a step of {step}', ylabel='time (s)',
    title='Suite complexity test')
    ax1.legend()
    ax1.grid()

    # Reference graph (theoric complexity)
    y2 = []
    for i in range (1,n+step,step) :
        #Choisir la fonction de référence ici
        y2.append(math.log(i))
    ax2.plot(x1,y2)  
    ax2.set(xlabel='n', ylabel='time (s)',
    title='O(log(n))')
    ax2.grid()
    
    #Saving results
    fig.savefig("suite.png")
    plt.show()

# Main function
def main(n,step,nb):
    #Array with the results(an array) of each test
    #itératif
    results1 = []
    #recursif
    results2 = []
    #Logarithmique (matrice)
    results3 = []
    #n data max
    n = int(n)
    #number of test to do 
    nb = int(nb)
    #step 
    step = int(step)

    #Selectionnez quels tests vous voulez effectuer
    for i in range(0,nb):	
        results1.append(testIteratif(n,i+1,nb,step))
    #for i in range(0,nb):
    #    results2.append(testRecu(n,i+1,nb,step))
    for i in range(0,nb):
        results3.append(testLoga(n,i+1,nb,step))
    print("PLOTTING RESULTS")
    plotting(results1,results2,results3,n,nb,step)
  

if __name__ == "__main__":
        #argv1 = n data, argv2 = step of n; argv3 = number of tests
        if(len(sys.argv) < 4):
            print("Utilisation : n step nb\nn maxixum \nstep saut entre chaque n\nnb nombre de tests a réaliser avec les même paramètres\n")
        else:
            main(sys.argv[1],sys.argv[2],sys.argv[3])