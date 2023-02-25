import itertools


def is_word(word):
    # This function checks if a word is an actual word.
    # You can replace this with your own implementation, for example
    # by checking if the word is in a dictionary file.
    return word == "test"


def generate_anagrams(word):
    # Generate all the possible permutations of the word
    anagrams = set(
        ["".join(permutation) for permutation in itertools.permutations(word)]
    )
    # Filter out the anagrams that are not actual words
    actual_words = set(anagram for anagram in anagrams if is_word(anagram))
    return actual_words


word = "test"
anagrams = generate_anagrams(word)
print(anagrams)
