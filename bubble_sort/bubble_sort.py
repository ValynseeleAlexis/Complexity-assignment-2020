#!/usr/bin/python
#Auteur Valynseele Alexis
#Licence 3 Informatique

import sys
import numpy
import matplotlib
import matplotlib.pyplot as plt
from timeit import default_timer as timer

# Implementing the bubble sort
def bubbleSort(arr,n:int): 
    
    start = timer()
    # Traverse through all array elements 
    for i in range(n): 
  
        # Last i elements are already in place 
        for j in range(0, n-i-1): 
  
            # traverse the array from 0 to n-i-1 
            # Swap if the element found is greater 
            # than the next element 
            if arr[j] > arr[j+1] : 
                arr[j], arr[j+1] = arr[j+1], arr[j]
    end = timer()
    return arr,(end-start)
    
# Run bubble sort with a random array of n numbers, number are between 0 and n*5
def execution(n:int):
    arr = numpy.random.randint(0,n*5,n)
    results = bubbleSort(arr,n)
    return results[1]  #return runtime

#Run one or several tests and return the results and write them to the disk
def test(n:int,id:int,nb:int,step:int):
    n = int(n)
    results = []
    with open(f'bubble_sort_results_n{id}.txt','w') as f:
        print(f'Runtime of the bubble_sort program for n going from 0 to {n}\n', file=f)
        start = timer()
        for i in range(0,n+step,step):
            runtime = execution(i)
            results.append(runtime)
            print(f"n = {i}\tRuntime = {runtime}", file=f)
            print(f"test n{id}/{nb} : {i} / {n} [OK]")
        end = timer()
        print(f"\n\nTotal runtime of the test session is {(end-start)} seconds", file=f)
        print(f"\nTotal runtime of the test session is {(end-start)} seconds")
        return results
        
#Plot the result + a comparaison of the theoric complexity      
def plotting(results,n:int,nb:int,step:int):
    #Setting up the plot
    fig, (ax1,ax2) = plt.subplots(1,2)
    x1 = range(0,n+step,step)
    x2 = numpy.linspace(0,n)
    
    #Plotting our results
    for i in range(0,nb):	
        ax1.plot(x1,results[i], label=f'test n°{i+1}')
    ax1.set(xlabel=f'n with a step of {step}', ylabel='time (s)',
    title='Bubble Sort complexity test')
    ax1.legend()
    ax1.grid()
    
    # Reference graph (theoric complexity)
    ax2.plot(x2,x2**2)
    
    ax2.set(xlabel='n', ylabel='time (s)',
    title='O(n^2)')
    ax2.grid()
    
    #Saving results
    fig.savefig("bubble_sort.png")
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
    
# Handling argv and running main      
if __name__ == "__main__":
        #argv1 = n data, argv2 = step of n; argv3 = number of tests
        main(sys.argv[1],sys.argv[2],sys.argv[3])

