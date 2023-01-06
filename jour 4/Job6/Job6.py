def valeur ():
    L = [1,2,3,4,5]
    swap = L[-1]
    L[-1] = L[0]
    L[0] = swap
    print (L)
valeur ()