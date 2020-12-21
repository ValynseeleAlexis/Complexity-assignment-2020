import matplotlib.pyplot as plt
import os

tab=[]

with open('.\\dataCribleDerastotene.txt','r') as fichier:
    for ligne in fichier:
        tab.append(float(ligne))
    plt.plot(tab)
    plt.show()




  





    
