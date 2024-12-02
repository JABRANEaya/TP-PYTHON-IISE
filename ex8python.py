def sum (*args):
    somme=0
    for i in args :
        somme+=i
     
    return somme
print("la somme des argument est:", sum(1,2,3,4))