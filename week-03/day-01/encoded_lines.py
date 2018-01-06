# Create a method that decrypts encoded-lines.txt

import string

alphabet_list = string.printable


def decrypt(filename):
    with open(filename) as f:
        content = list(f.read())
    for i in range(0, len(content)):
        if content[i] == " ":
            content[i] = " "
        elif content[i] != "\n":
            content[i] = alphabet_list[int(alphabet_list.index(content[i]))-1]
    return "".join(content)


print(decrypt("encoded-lines.txt"))
