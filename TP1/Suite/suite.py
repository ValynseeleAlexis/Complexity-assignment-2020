#!/usr/bin/python
#Auteur Valynseele Alexis
#Licence 3 Informatique

import sys
import numpy
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

#Run one or several tests and return the results and write them to the disk
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

#Run one or several tests and return the results and write them to the disk
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
     
#Plot the result + a comparaison of the theoric complexity      
def plotting(results1,results2,n:int,nb:int,step:int):
    #Setting up the plot
    fig, (ax1,ax2) = plt.subplots(1,2)
    x1 = range(0,n+step,step)
    x2 = numpy.linspace(0,n)
    
    #Plotting our results
    for i in range(0,nb):	
        ax1.plot(x1,results1[i], label=f'test n°{i+1} iteratif')
        ax1.plot(x1,results2[i], label=f'test n°{i+1} recursif')
    ax1.set(xlabel=f'n with a step of {step}', ylabel='time (s)',
    title='Suite complexity test')
    ax1.legend()
    ax1.grid()

    # Reference graph (theoric complexity)
    ax2.plot(x2,x2)
    
    ax2.set(xlabel='n', ylabel='time (s)',
    title='O(n)')
    ax2.grid()
    
    #Saving results
    fig.savefig("suite.png")
    plt.show()

# Main function
def main(n,step,nb):
    #Array with the results(an array) of each test
    results1 = []
    results2 = []
    #n data max
    n = int(n)
    #number of test to do 
    nb = int(nb)
    #step 
    step = int(step)

    for i in range(0,nb):	
        results1.append(testIteratif(n,i+1,nb,step))
    for i in range(0,nb):
        results2.append(testRecu(n,i+1,nb,step))
    print("PLOTTING RESULTS")
    plotting(results1,results2,n,nb,step)
  

if __name__ == "__main__":
        #argv1 = n data, argv2 = step of n; argv3 = number of tests
        if(len(sys.argv) < 4):
            print("Utilisation : n step nb\nn maxixum \nstep saut entre chaque n\nnb nombre de tests a réaliser avec les même paramètres\n")
        else:
            main(sys.argv[1],sys.argv[2],sys.argv[3])