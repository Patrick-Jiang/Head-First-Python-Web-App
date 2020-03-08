# def search4vowels():
#     vowels = set('aeiou')
#     word = input("Provide a word to search for vowels: ")
#     found = vowels.intersection(set(word))
#     for vowel in found:
#         print(vowel)


# def search4vowels(word: str) -> set:
#     vowels = set('aeiou')
#     # word = input("Provide a word to search for vowels: ")
#     found = vowels.intersection(set(word))
#     # for vowel in found:
#     #     print(vowel)
#     # return bool(found)
#     return found


# help(search4vowels)

def search4vowels(phrase: str) -> set:
    """Return any vowels found in a supplied phrase."""
    vowels = set('atiou')
    return vowels.intersection(set(phrase))


def search4letters(phrase: str, letters: str = 'aeiou') -> set:
    """"Return a set of the 'letter' found in 'phrase'. """
    return set(letters).intersection(set(phrase))


# help(search4letters)
# print(search4letters('dsadasdas', 'dsadas'))

# print(search4letters(letters='xyz', phrase='galaxy'))
