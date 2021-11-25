"""This script computes interesting stats about a file (such as a book)
available in .txt format)."""

from sequenceTools import *
# imports all variables defined in __all__ in module sequenceTools


# ignore this function for now 
def readWords(filename):
    """Given a path to a file as a string, it returns the list of all 
    words in it"""
    wordList = [] # list accumulation variables
    with open(filename) as myfile: # open file reading
        for line in myfile:  # iterate over lines in file
            line = line.strip() #strip spaces at the beg and end
            wordList += line.split()
    # implicit close file
    return wordList

# lets find out how many words in the file start and end with the same letter (pretty words)

def prettyWords(wordList):
    """Returns a list of words that start and end with the same letter from the given list.
    >>> prettyWords(['Nun', 'Sun', 'gun', 'tot'])
    ['Nun', 'tot']
    """
    return wordStartEnd(wordList)


def uniquePalindromes(wordList):
    """Returns a list of unique palindromes of length greater than 1 in the given wordList
    >>> uniquePalindromes(['Madam', 'Mary', 'is', 'Wow'])
    ['Madam', 'Wow']
    >>> uniquePalindromes(['a', 'a', 'bb', 'bb', 'aaa'])
    ['bb', 'aaa']
    """
    pass 


def commonWords(wordList1, wordList2):
    """Takes two wordlists and returns the common words in them (ignoring case) in lower case
    >>> commonWords(['hello', 'World'], ['Hello', 'Earth'])
    ["hello"]
    """
    pass




#  word with the most number of vowels in the book?
def mostVowelWord(wordList):
    """Takes a wordList and returns the word with the most number of vowels
    >>> mostVowelWord(['birds', 'of', 'a', 'feather'])
    'feather'
    """
    pass




if __name__ == '__main__':
    #testing code here
    import doctest
    doctest.testmod()
    wordList = readWords('textfiles/prideandprejudice.txt')
    #print(wordList)
    #print('Total number of words:', len(set(wordList)))
    #print('The number of pretty words in Pride and Prejudice', len(prettyWords(wordList)))
    #print('The word in Pride and Prejudice with the most number of vowels', mostVowelWord(wordList))
    #print('Names common in names of this class and Pride and Prejudice:')
    #classNames = fileToWordList('textfiles/classNames.txt')
    #print(set(commonWords(classNames, wordList)))
    #print('The palindromes in Pride and Prejudice are: ', *uniquePalindromes(wordList))
