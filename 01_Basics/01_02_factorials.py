# Note: Factorials do not exist for negative numbers and fractions
#

def fact(num):
    if type(num) != int or num < 0:
        return None

    if num == 0:
        return 1
    
    result = 1
    loopvar = 1
    while (loopvar <= num):
        result *= loopvar
        loopvar += 1
    
    return result

def factrecursive(num):
    if type(num) != type(1) or num < 0:
        return None

    if num == 0:
        return 1

    return num * factrecursive(num-1)

print(fact(6))
print(fact(2.4))
print(fact(-2))

print(factrecursive(6))
print(factrecursive(2.4))
print(factrecursive(-2))