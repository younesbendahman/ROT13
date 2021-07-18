import string as s
import sys

caesar_alphabet = {}
alphabet = s.ascii_lowercase

for i in range(len(alphabet)):
    if i + 13 >= 26:
        temp = i + 13 - 26

    else:
        temp = i + 13

    caesar_alphabet[alphabet[i]] = alphabet[temp]

def convert(txt:str):
    txt.lower()
    output = ""

    for i in txt:
        if i in alphabet:
            output += caesar_alphabet[i]
        else:
            output += i

    return output

if __name__ == "__main__":
    for i in sys.argv[1:]:
        print(convert(i), end=" ")


