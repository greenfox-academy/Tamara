# Create a method that decrypts reversed-lines.txt


def decrypt(file_name):
    with open(file_name, "r") as f:
        text = f.read()
        reversed = text[::-1]
    print(reversed)

    f.close()
decrypt("reversed_lines.txt")