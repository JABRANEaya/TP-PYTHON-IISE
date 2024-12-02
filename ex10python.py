def fusionner_dicts(dictionnaire1, dictionnaire2):
    fusion=dictionnaire1.copy()
    for cle, valeur in dictionnaire2.items():
        if cle in fusion:
            fusion[cle]+= valeur
        else:
            fusion[cle]= valeur
        return fusion
dictionnaire1={"aya":3 ,"khalid":2, "israe":1}
dictionnaire2={"nada":3, "nora":2, "rachida":1}
print(fusionner_dicts(dictionnaire1, dictionnaire2))