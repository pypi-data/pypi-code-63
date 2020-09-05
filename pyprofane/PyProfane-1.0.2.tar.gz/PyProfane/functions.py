from PyProfane.constants import censorSymbols, censorSymbolsLength, letterMappings, lettersToRemove, profaneWordSoundex, profaneWordsSoundexValues, profaneWords
from typing import List
import re
import random
try:
    from pprint import pprint
    printVersion = 1
except:
    printVersion = 0

def soundex(term: str) -> str:
    '''
    Return soundex
    '''
    query = term.lower()
    letters = [char for char in query if char.isalpha()]

    if len(letters)!=len(query):
        return term

    firstLetter = letters[0]

    letters = [char for char in letters[1:] if char not in lettersToRemove]

    for i in range(len(letters)):

        letters[i] = letterMappings[letters[i]]

    j = 0
    for i in range(1,len(letters)):
        if letters[j] != letters[i]:
            j+=1
            letters[j] = letters[i]
    
    if len(letters)>=3:
        letters = [str(i) for i in letters][:3]
    else:
        while(len(letters) < 3):
            letters.append(0)
        letters = [str(i) for i in letters][:3]

    sound = firstLetter.upper() + ''.join(letters)

    return sound

def censorWord(word: str) -> str:
    '''
    Censor word.
    '''
    term = list(word)
    length = len(term)
    if length <= 4:
        term[1] = censorSymbols[random.randint(0,censorSymbolsLength-1)]
    if length > 4:
        censorPositions = random.sample(range(1,length-2), length//2)
        for i in censorPositions:
            term[i] = censorSymbols[random.randint(0,censorSymbolsLength-1)]
    
    return ''.join(term)


def censorSentences(comments: List[str]) -> List[str]:
    '''
    Censor a list of sentences based on soundex values and set of characters.
    Please note that this is my personal approach and based off no research as far as I am aware of.
    Future: I feel Levenshtien distance can be used to exploit this further.
    '''

    sentences = []

    for i in comments:
        soundexComment = i
        allWords = re.findall(r"[\w']+|[.,!?;]", i)
        for j in allWords:
            value = soundex(j)
            if value in profaneWordsSoundexValues:
                keys = getAllKeysFromValues(profaneWordSoundex,value)
                for key in keys:
                    if set(j) == set(key):
                        soundexComment = soundexComment.replace(j,censorWord(j))
        sentences.append(soundexComment)

    return sentences

def updateSwearwords(filename: str) -> int:
    '''
    Update your swearwords based on your own text files
    '''

    global profaneWordSoundex, profaneWordsSoundexValues, profaneWords

    f = open(filename,'r')
    words = f.read().splitlines()
    yourSoundex = dict()

    for i in words:
        yourSoundex[i] = soundex(i)
    
    profaneWordSoundex = yourSoundex
    profaneWordsSoundexValues = list(yourSoundex.values())
    profaneWords = list(yourSoundex.keys())

    print('**Your soundex was successfully updated**')

    return 0

def isProfane(sentence: str) -> bool:
    '''
    Function that returns if a sentence is profane or not.
    '''

    allWords = re.findall(r"[\w']+|[.,!?;]", sentence)
    for j in allWords:
        value = soundex(j)
        if value in profaneWordsSoundexValues:
            keys = getAllKeysFromValues(profaneWordSoundex,value)
            for i in keys:
                if set(j) == set(i):
                    return True
    
    return False

def getProfaneWords():
    '''
    Prints a list of current profane/swear words
    '''

    if printVersion:
        pprint(profaneWords)
    else:
        print(profaneWords)

def getAllKeysFromValues(mapping: dict, searchValue: str) -> List[str]:
    '''
    Helper function.
    Future: can be moved into another file with the name helpers.py later
    '''

    return [key for (key,value) in mapping.items() if value == searchValue]
