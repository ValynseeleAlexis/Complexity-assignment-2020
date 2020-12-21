#!/usr/bin/python
#Auteur Valynseele Alexis
#Licence 3 Informatique

import sys
import numpy
import matplotlib
import matplotlib.pyplot as plt
from timeit import default_timer as timer

def CribleEratosthenes(prime,n): 
    p = 2
    while (p * p <= n): 
          
        # Si on update pas prime[p] alors il est premier
        if (prime[p] == True): 
              
            # On update tout les multiples de p
            for i in range(p * 2, n + 1, p): 
                prime[i] = False
        p += 1
    #On peut skip 0 et 1 car on sait qu'il ne sont pas premier
    prime[0]= False
    prime[1] = False
    return prime

def EratostehnesExecution(n):
    #On part du principe que tout les nobmres entre 0 et n sont premiers, les indices representent les nombres
    prime = [] 
    for i in range(0,n+1):
        prime.append(True)
    #starting the timer
    start = timer()
    CribleEratosthenes(prime,n)
    end = timer()
    return (end-start)

#Run one test and return the results and write them to the disk
#n data,id ,nb number of test,step is the step between each n
def test(n:int,id:int,nb:int,step:int):
    n = int(n)
    results = []
    with open(f'CribleEratosthenes_results_n{id}.txt','w') as f:
        print(f'Runtime of the Eratosthenes for n going from 2 to {n+2}\n', file=f)
        start = timer()
        for i in range(2,n+step,step):
            runtime = EratostehnesExecution(i)
            results.append(runtime)
            print(f"n = {i}\tRuntime = {runtime}", file=f)
            #print(f"test n{id}/{nb} : {i} / {n} [OK]")
        end = timer()
        print(f"\n\nTotal runtime of the test session is {(end-start)} seconds", file=f)
        print(f"\nTotal runtime of the test session is {(end-start)} seconds")
        return results
     
#Plot the result + a comparaison of the theoric complexity      
def plotting(results,n:int,nb:int,step:int):
    #Setting up the plot
    fig, (ax1,ax2) = plt.subplots(1,2)
    x1 = range(2,n+step,step)
    
    #Calcul moyenne de tout les tests
    moyenne = []
    calulMoyenne = 0
    for i in range(0,len(x1)):
        for j in range(0,nb):
            calculMoyenne = calulMoyenne  + results[j][i]
        calculMoyenne / nb
        moyenne.append(calculMoyenne)
    with open(f'eratosthene_moyenne.txt','w') as f:
        print(f'Average runtime of the eratosthene program for n going from 0 to {n+2} with {nb} tests\n', file=f)
        for i in range(0,len(x1)):
            print(f"n = {(i*step)+2}\tRuntime = {moyenne[i]}", file=f)

    #Plotting our results
    #for i in range(0,nb):	
        #ax1.plot(x1,results[i], label=f'test Eratosthenes n°{i+1}')
    ax1.plot(x1,moyenne,label=f'moyenne de {nb} tests')
    ax1.set(xlabel=f'n with a step of {step}', ylabel='time (s)',
    title='Eratosthenes complexity test')
    ax1.legend()
    ax1.grid()
    
    # Reference graph (theoric complexity)
    y2 = []
    for i in range (2,n+step,step) :
        #Choisir la fonction de référence ici
        y2.append(i)
    ax2.plot(x1,y2)
    ax2.set(xlabel='n', ylabel='time (s)',
    title='O(n)')
    ax2.grid()
    
    #Saving results
    fig.savefig("eratosthenes.png")
    plt.show()

# Main function
def main(n,step,nb):
    #Array with the results(an array) of each test
    results = []
    #n data max
    n = int(n)
    #number of test to do 
    nb = int(nb)
    #step 
    step = int(step)

    for i in range(0,nb):	
        results.append(test(n,i+1,nb,step))
    print("PLOTTING RESULTS")
    plotting(results,n,nb,step)

if __name__ == "__main__":
        #argv1 = n data, argv2 = step of n; argv3 = number of tests
        if(len(sys.argv) < 4):
            print("Utilisation : n step nb\nn maxixum \nstep pas entre chaque n\nnb nombre de tests a réaliser avec les même paramètres\nExemple 30 1 1 va réaliser un test qui executra hanoi pour n allant de 1 à 30 et ceux 1 fois")
        else:
            main(sys.argv[1],sys.argv[2],sys.argv[3])