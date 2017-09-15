
#word = input("Please, write a word which contains at least 3 syllable! ")
def anagram ():
    words = ["car", "race", "rac", "ecar", "me", "em"]
    anagrams = {}
    for word in words:
        if sorted(word) == word[::-1]:
            return True
        if reverse_word in words:
            anagrams[word] = (words.index(reverse_word))

anagram()