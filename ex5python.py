def factorielle(n):
    while True:
    n= int(input ("entrer la valeur de nombre n :"))
    if n>0:
        break
    
        if n==0:
            return 1
        else:
            f=1
            for i in range(2,n+1):
                f=f*i
                return f
print(factorielle(n))

