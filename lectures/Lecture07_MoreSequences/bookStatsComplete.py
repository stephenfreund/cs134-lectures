"""This script computes interesting stats about the book Pride and Prejudice (or any other book
available in .txt format)."""


from sequenceTools import * # imports all variables defined in __all__ in module sequenceTools

def fileToWordList(filename):
    """Given a file name it returns the list of words in it"""
    wordList = []
    with open(filename) as book:  # with block for opening file
        for line in book:  # iterate over each line (ending with \n)
            line = line.strip()  # .strip() removes leading and trailing whitespace.
            # .split will split a string into a list
            # based on a character (default is a space)
            wordList += line.split()
    return wordList


# how many words in the file start and end with the same letter (pretty words)

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
    allPalindromes = palindromes(wordList)
    result = [] # initilize list accumulator variable
    for word in allPalindromes:
        if len(word)>1 and word not in result:
            result.append(word)
    return result


def commonWords(wordList1, wordList2):
    commonW = []
    for word1 in wordList1:
        for word2 in wordList2:
            if word1.lower() == word2.lower():
                commonW.append(word1)
    return commonW

 
#  words with the most number of vowels?
def mostVowelWord(wordList):
    maxVowelNum = 0
    maxVowelWords = []
    for word in wordList:
        numVowels = countVowels(word)
        if numVowels > maxVowelNum:
            maxVowelNum = numVowels
            maxVowelWord = [word]
        elif numVowels == maxVowelNum:
            maxVowelWord.append(word)
    return maxVowelWord



if __name__ == '__main__':
    import doctest
    doctest.testmod()
    #testing code here
    wordList = fileToWordList('textfiles/prideandprejudice.txt')
    #print(fileToWordList('textfiles/prideandprejudice.txt'))
    #print('The word in Pride and Prejudice with the most number of vowels', mostVowelWord(wordList))
    #print('The number of pretty words in Pride and Prejudice', len(prettyWords(wordList)))
    #print('Names common in names of this class and Pride and Prejudice:')
    #classNames = fileToWordList('textfiles/classNames.txt')
    #print(set(commonWords(classNames, wordList)))
    #print('The palindromes in Pride and Prejudice are: ', *uniquePalindromes(wordList))

