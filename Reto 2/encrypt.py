from string import ascii_lowercase

ascii_codes = [ord(char) for char in ascii_lowercase]

def decrypt(code: str) -> str:

    tmp = ''
    phrase = ''
    
    for n in code:
        if n == " ":
            phrase += " "
            continue

        tmp += n
        if int(tmp) in ascii_codes:
            phrase += chr(int(tmp))
            tmp = ''

    return phrase

with open("encrypted.txt") as file:
    code = file.read()
    phrase = decrypt(code)
    print(phrase)