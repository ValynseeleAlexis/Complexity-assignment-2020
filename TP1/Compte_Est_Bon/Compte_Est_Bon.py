


tab = [1, 2, 3]



def fonct(tabCount):
    
    tabTemp=tabCount.copy()
    for i in range(0,len(tabTemp)):   #de 0 à 2
        for j in range(i+1,len(tabTemp)): # 1 à 2
            print(str(i) +" "+ str(j))
            if(i!=j):
                #print(tabCount)
                x=tabCount[i]
                y=tabCount[j]
                tabCount.append(tabCount[i]+tabCount[j])
                tabCount.remove(x)
                tabCount.remove(y)
                fonct(tabCount)


fonct(tab)



