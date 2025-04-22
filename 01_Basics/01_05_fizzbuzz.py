
def fizzbuzz1(num):
    for i in range(num+1):
        if i%6 == 0:
            print("FizzBuzz")
        elif i%2 == 0:
            print("Fizz")
        elif i%3 == 0:
            print("Buzz")
        else:
            print(i)

def fizzbuzz2(num):
    for i in range(num+1):
        # result = "FizzBuzz" if i%6==0 else "Fizz" if i%2==0 else "Buzz" if i%3 == 0 else i
        print(f"FizzBuzz" if i%6==0 else "Fizz" if i%2==0 else "Buzz" if i%3 == 0 else i) 

def main():
    fizzbuzz1(15)
    print("-------")
    fizzbuzz2(15)

if __name__ == "__main__":
    main()