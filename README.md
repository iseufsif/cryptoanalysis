# Monoalphabetic Cryptoanalysis

## Approach

### What do I need?
- I need an input field to put in the enciphered message
- I need a file which holds letter counts of the english language
  - later on I can maybe support multiple languages
  - later on I can maybe also support word counts, word lengths, letter counts by position within a word, bigram counts and more
  - maybe in form of a hash table or KVS (letter being the key, the % being the lookup value)
- I need a function to count the characters of the enciphered message
- I need a function which calculates letter distribution of the enciphered message's letters
- I need a function which compares the calculated frequency with the English frequency and calculates the most likely match
- I need an output of the deciphered message
- I need to be able to correct or interact with the output to do multiple loops suggesting different matches

### What would be really cool?
- If the program could recognize words and fix semi-deciphered messages by looking for likely matches for a word (e.g. through an API)
- 