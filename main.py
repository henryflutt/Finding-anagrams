# Check if two words are anagrams 
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True


def find_anagram(word, anagram):
    # [assignment] Add your code here
    word = input('Please enter your first word: ')
    anagram = input('Please enter your second word: ')
    #Check if both words are of the same length
    if len(word) == len(anagram):
        #re-arrange strings
        sort_word = sorted(word).lower()
        sort_anagram = sorted(anagram).lower()
        #check if strings are the same
        if (sort_word) == (sort_anagram):
            return True
        else:
            return False
    else:
        False


