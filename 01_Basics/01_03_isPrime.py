

import math

def isPrime(num):
    if type(num) != int  or num < 2:
        return False
    
    if num in [2,3]:
        return True
    
    for i in range(2, int(math.pow(num,0.5))+1):
        if(num%i == 0):
            return False
        
    return True

print(isPrime(0))
print(isPrime(1))
print(isPrime(2))
print(isPrime(30))
print(isPrime(71))
