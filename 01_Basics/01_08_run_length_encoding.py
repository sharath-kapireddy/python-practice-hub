## Input AAAAAbbBCCCC -> 5A3B4C


def encoder(input_str):
    input_str = input_str.strip().upper()
    
    if (input_str is None or len(input_str) == 0 ):
        return None
    
    if(len(input_str) == 1):
        return "1"+input_str
    
    prevChar, counter = input_str[0], 1
    res = ""

    for ch in input_str[1:]:
        if (ch == prevChar):
            counter += 1
        else:
            res = res  + str(counter) + prevChar
            prevChar= ch
            counter = 1

    res = res  + str(counter) + prevChar
    return res

def decoder(enc_str):
    # Assuming the input is a valid encoded str

    res = ""
    for i, ch in enumerate(enc_str):
        if(i%2 != 0):
            continue

        cnt = int(ch)
        part_res = ""
        for _ in range(cnt):
            part_res += enc_str[i+1]
        res += part_res
    
    return res

if __name__ == "__main__":
    print(encoder("AAAAAbBBCCcCACCC"))
    print(encoder("AAAB"))
    print(decoder("5A6B2C"))

