"""This module contains different functions that iterate over sequences such as strings and list.

You can query this documentation using pydoc3 sequenceTools from the terminal"""

# When this module is imported with
#   from sequenceTools import *
# __all__ keeps track of all the symbols you want the importer to receive:
__all__ = [ "countVowels", "countChar", "vowelSeq"]

# All functions go below here.

def isVowel(char):
    """Returns true a given letter is a vowel .
    >>> isVowel('e')
    True
    >>> isVowel('U')
    True
    >>> isVowel('t')
    False
    >>> isVowel('Z')
    False
    """
    return char.lower() in 'aeiou'


def countVowels(word):
    '''Returns number of vowels in the word.
    >>> countVowels('Williams')
    3
    >>> countVowels('Eephs')
    2'''
    count = 0 # initialize the counter
    for char in word: # iterate over the word one character at a time
        if isVowel(char):
            count += 1
    return count

def countChar(char, word):
    '''Counts the number of times a character appears in a word.
    >>> countChar('a', 'Alabama')
    4
    >>> countChar('E', 'Eephs')
    2'''
    count = 0
    for letter in word:
        if char.lower() == letter.lower():
            count += 1
    return count

def vowelSeq(word):
    '''returns the vowel subsequence in given word.
    >>> vowelSeq("Chicago")
    'iao'
    >>> vowelSeq("protein")
    'oei'
    >>> vowelSeq("rhythm")
    ''
    '''
    vowels = ""
    for char in word:
        if isVowel(char):
            vowels += char
    return vowels

if __name__ == "__main__":
    import doctest
    doctest.testmod()
    #if you want to see output even when tests pass, set optional argument verbose=True
    # that is, doctest.testmod(verbose=True)
