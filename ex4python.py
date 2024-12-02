def compte_occurences(liste):
    dictionnaire = {}
    for i in liste:
        dictionnaire[i]=liste.count(i)
            
    return dictionnaire

liste = ['aya', 'nora', 'assia', 'nora', 'aya', 'aya', 'aya']
print(compte_occurences(liste))



#methode 2 

def compte_occurences(liste):
    dictionnaire = {}
    for i in liste:
        if i in dictionnaire:
            dictionnaire[i]+=1
        else:
            dictionnaire[i]=1
    return dictionnaire
liste = ['aya', 'nora', 'assia', 'nora', 'assia', 'aya', 'aya']
print(compte_occurences(liste))
