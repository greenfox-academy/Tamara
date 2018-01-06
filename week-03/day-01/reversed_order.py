# Create a method that decrypts reversed-order.txt


def decrypt(file_name):
    with open(file_name, "r") as f:
        text = f.read()
        reversed_content = text[::-1]
    return reversed_content


print(decrypt("reversed_order.txt"))
