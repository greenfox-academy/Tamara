# Create a method that decrypts the duplicated-chars.txt

def decrypt(file_name):
    with open(file_name, "r") as f:
        text = f.read()
        decrypted = text[::2]
    print(decrypted)


decrypt("duplicated_chars.txt")
