def prime(x):
    totalFactors=0
    for i in range(1, x+1):
        if factor(i,x):
            totalFactors += 1
    if (totalFactors<=2):
        return True
    else:
        return False