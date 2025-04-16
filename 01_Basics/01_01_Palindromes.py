# TASK : Return a Boolean value indicating whether the string is a palindrome. 
# A palindrome is a string that reads the same forward and backward, ignoring spaces, capitalization, and punctuation 


def is_palindrome(str):
    str = str.strip().lower()
    formattedstr = ""

    for chr in str:
        if chr.isalnum():
            formattedstr= formattedstr+chr
    return formattedstr == formattedstr[::-1]


def main():
    inputList = ["abc Cba", "Hello!", "! HeollOeh"]

    result = 0
    for word in inputList:
        result += is_palindrome(word)
    print("Total palindromes", result)

if __name__ == "__main__":
    main()