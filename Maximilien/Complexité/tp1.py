import matplotlib.pyplot as plt
import os

tab=[]

with open('C:\\Users\\wmaxi\\Desktop\\Cours FAC\\Licence 3\\Complexité\\dataSuiteIte.txt','r') as fichier:
    for ligne in fichier:
        tab.append(float(ligne))
    plt.plot(tab)
    plt.show()




    
