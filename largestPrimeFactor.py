n = 600851475143
maxNum = -1

def getFactors(n):
    factors = list()
    for i in range(1, int(n**(1/2))+1):
        if n%i == 0:
            factors.append(i)
    return factors

def isPrime(fact):
    primeList = list()
    for i in range(1,fact+1):
        if fact%i == 0:
            primeList.append(i)
    return len(primeList) == 2

factors = getFactors(n)
for i in factors:
    if isPrime(i) and i > maxNum:
        maxNum = i
print(maxNum)