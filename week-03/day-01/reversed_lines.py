# Create a method that decrypts reversed-lines.txt


def decrypt(file_name):
    with open(file_name, "r") as f:
        text = f.read()
        reversed_text = text[::-1]
    return reversed_text


print(decrypt("reversed_lines.txt"))
