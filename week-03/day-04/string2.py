# Given a string, compute recursively a new string where all the 'x' chars have been removed.

def recursive_remove_char(word):
    if word == "":
        return word
    elif word[0] == "x":
        return "" +  recursive_remove_char(word[1:])
    else:
        return word[0] + recursive_remove_char(word[1:])

print(recursive_remove_char("Relax"))
