# Given a string, compute recursively (no loops) a new string where all the
# lowercase 'x' chars have been changed to 'y' chars.

def recursive_string(word):
    if word == "":
        return word
    elif word[0] == "x":
        return "y" +  recursive_string(word[1:])
    else:
        return word[0] + recursive_string(word[1:])

print(recursive_string("Rexax"))


