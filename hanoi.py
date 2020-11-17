#!/usr/bin/python

import sys
from timeit import default_timer as timer

def hanoi(n, src, aux, dest):    
    if n == 1:
        #print ("Transferer le disque 1 de",src,"vers",dest)
        return
    hanoi(n-1, src, dest, aux)
    #print ("Transferer le disque",n,"de",src,"vers",dest)
    hanoi(n-1, aux, src, dest)

def main(n):
    if n == 0:
        print("Erreur: Il faut au moins 1 disque")
    else:
        #starting the timer
        start = timer()
        hanoi(int(n),'A','B','C')
        end = timer()
        print(f"Total runtime of the program is {end - start}") 

if __name__ == "__main__":
    main(sys.argv[1])
