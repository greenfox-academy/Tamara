# Given a string, compute recursively a new string where all the
# adjacent chars are now separated by a "*".

def recursive_string_separating(word):
    if len(word) == 1:
        return word
    else:
        return word[0] + "*" + recursive_string_separating(word[1:])

print(recursive_string_separating("Relax"))
