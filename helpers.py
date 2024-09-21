import constants as c
import re
import wordPatterns


def translateMessage(key, message, mode):
    translated = ''
    charsA = c.LETTERS
    charsB = key
    if mode == 'decrypt':
        # For decrypting, we can use the same code as encrypting. We
        # just need to swap where the key and LETTERS strings are used.
        charsA, charsB = charsB, charsA

    # Loop through each symbol in the message:
    for symbol in message:
        if symbol.upper() in charsA:
            # Encrypt/decrypt the symbol:
            symIndex = charsA.find(symbol.upper())
            if symbol.isupper():
                translated += charsB[symIndex].upper()
            else:
                translated += charsB[symIndex].lower()
        else:
            # Symbol is not in LETTERS; just add it:
            translated += symbol
    return translated


def enumerateWord(word):
    encountered = {}
    numbered_word = ''
    for char in word:
        if char not in encountered:
            encountered[char] = len(encountered)

        numbered_word += (str(encountered[char]) + ".")

    numbered_word = numbered_word[:-1]
    return numbered_word


def decryptMessage(key, message):
    return translateMessage(key, message, 'decrypt')


class EncipheredMessage:
    def __init__(self):
        self.enciphered_message = ''
        self.counter = c.NULL_LETTER_COUNT.copy()
        self.percentages = c.NULL_LETTER_COUNT.copy()
        self.letterMapping = c.BLANK_LETTER_MAPPING.copy()
        self.solvedMapping = c.BLANK_LETTER_MAPPING.copy()
        self.removeNonLetters = re.compile(r'[^A-Z\s]')

    def getEncipheredMessage(self):
        self.enciphered_message = input("Insert the enciphered message here: ").upper()

    """
    def countChars(self):
        for char in self.enciphered_message:
            if char in self.counter:
                self.counter[char] += 1

        print(self.counter)
        return self.counter

    def calcPercentage(self):
        total_letters = sum(self.counter.values())
        for i in self.counter:
            percent = round(self.counter[i] / total_letters, 5)
            self.percentages[i] = percent

        print(self.percentages)
        return self.percentages
    """

    def addLettersToMapping(self, cipherword, decipheredCandidate):
        for i in range(len(cipherword)):
            if decipheredCandidate[i] not in self.letterMapping[cipherword[i]]:
                self.letterMapping[cipherword[i]].append(decipheredCandidate[i])

    def removeSolvedLettersFromMapping(self, letterMapping):
        looping = True
        while looping:
            looping = False
            solvedLetters = {}

            # Identify solved letters
            for cipherLetter in c.LETTERS:
                if len(letterMapping[cipherLetter]) == 1:
                    solvedLetters[cipherLetter] = letterMapping[cipherLetter][0]
                    self.solvedMapping[cipherLetter] = letterMapping[cipherLetter][0]

            # Remove solved letters from other entries
            for cipherLetter in c.LETTERS:
                for solvedLetters in self.solvedMapping:
                    if len(letterMapping[cipherLetter]) > 1 and solvedLetters in letterMapping[cipherLetter]:
                        letterMapping[cipherLetter].remove(solvedLetters)
                        if len(letterMapping[cipherLetter]) == 1:
                            looping = True

        return letterMapping

    def hack(self):
        wordList = self.removeNonLetters.sub('', self.enciphered_message).split()

        for cipherword in wordList:
            wordPattern = enumerateWord(cipherword)
            if wordPattern not in wordPatterns.allPatterns:
                continue
            for candidateWord in wordPatterns.allPatterns[wordPattern]:
                self.addLettersToMapping(cipherword, candidateWord)

        return self.removeSolvedLettersFromMapping(self.letterMapping)

    def decryptWithMapping(self):
        key = ['x'] * len(c.LETTERS)
        for cipherletter in c.LETTERS:
            if len(self.solvedMapping[cipherletter]) == 1:
                keyIndex = c.LETTERS.find(self.solvedMapping[cipherletter][0])
                key[keyIndex] = cipherletter

        key = ''.join(key)
        return decryptMessage(key, self.enciphered_message)