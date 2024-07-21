def print_upper_words2(words):
    """For a list of words, print out each word on a 
    separate line, but in all uppercase"""
    for word in words:
        print(word.upper())

def print_upper_words3(words):
    """For a list of words, only prints words that start with the letter 'e' or 'E' on 
    each separate line, in all uppercase"""
    for word in words:
        if word[0] == "e" or word[0]=="E":
            print(word.upper())


def print_upper_words4(words,must_start_with):
    """For a list of words, print out each word that start with one of the given letters on a 
    separate line in all uppercase"""
    for word in words:
        for letter in must_start_with:
            if word[0].upper() == letter.upper():
                print(word.upper())