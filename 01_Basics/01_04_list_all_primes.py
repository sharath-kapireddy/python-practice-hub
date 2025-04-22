import math

def allPrimes(num):
    num = int(num)

    if (num < 2):
        return []
    
    primesFound = [2]

    for i in range(2, num+1):
        for prime in primesFound:
            if (i%prime == 0):
                break
        else:
            primesFound.append(i)
    
    return primesFound

def printAllPrimes(num):
    for i in range(2, num+1):
        for j in range(2, int(math.pow(i, 0.5)+1)):
            if (i%j == 0):
                break
        else:
            print(f"{i} is prime")

def main():
    print(allPrimes(100))
    printAllPrimes(30)

if __name__ == "__main__":
    main()