"""This module contains different functions that iterate over sequences such as strings and list.

You can query this documentation using pydoc3 sequenceTools from the terminal"""

# When this module is imported with
#   from sequenceTools import *
# __all__ keeps track of all the symbols you want the importer to receive:
__all__ = [ "vowelSeq", "countVowels", "countItem", "wordStartEnd", "palindromes"]

# All functions go below here.

def isVowel(char):
    """Takes a letter as input and returns true if and only if it is a vowel."""
    return char.lower() in 'aeiou'



def countItem(seq, el):
    '''Takes as input a sequence seq (can be a string or a list), 
    and an element el and returns the number of times el appears 
    in the sequence seq.'''
    count = 0
    for item in seq:
        if item == el:
            count += 1
    return count

def vowelSeq(word):
    '''returns the vowel subsequence in given word.
    '''
    vowels = ""
    for char in word:
        if isVowel(char):
            vowels += char
    return vowels


def countVowels(word):
    '''Returns number of vowels in the given word.'''
    # can use vowelSeq function
    return len(vowelSeq(word))


def wordStartEnd(wordList):
    '''Takes a list of words and counts the 
    number of words in it that start and end 
    with the same letter'''
    # initialize accumulation variable (of type list)
    result = []
    for word in wordList: # iterate over list
        
        #check for empty strings before indexing
        if len(word) != 0:  # can also write 
            if word[0].lower() == word[-1].lower():
                result += [word] # concatenate to resulting list
    return result # notice the indentation of return


def palindromes(sList):
    '''Takes a list of words and counts the 
    number of words in it that start and end 
    with the same letter'''
    # initialize accumulation variable (of type list)
    result = []
    for word in sList: # iterate over list
        wLower = word.lower()
        if wLower[::-1] == wLower:  
            result += [word] # concatenate to resulting list
    return result 

