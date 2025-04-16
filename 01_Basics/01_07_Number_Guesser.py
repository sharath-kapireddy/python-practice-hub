
import random

number = random.randint(1,100)
print(number)

choice = input("Guess the number:")
cnt = 0

while(True):
    choice = int(choice)
    cnt += 1
    if choice == number:
        break
    elif choice < number:
        choice = input("Guess a larger number:")
    else :
        choice = input("Guess a smaller number:")

print(f"The right answer was {number} and it took you {cnt} attempts")
