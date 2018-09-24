from data import DICTIONARY, LETTER_SCORES

def load_words():
    """Load dictionary into a list and return list"""
    file = open(DICTIONARY)
    lst_words = [word.replace('\n', '') for word in file]
    file.close()
    return lst_words

def calc_word_value(word):
    """Calculate the value of the word entered into function
    using imported constant mapping LETTER_SCORES"""
    total = 0
    for l in word.upper():
        if l in LETTER_SCORES.keys():
            total += LETTER_SCORES[l]
    return total

def max_word_value(list_words = None):
    """Calculate the word with the max value, can receive a list
    of words as arg, if none provided uses default DICTIONARY"""
    if not list_words:
        list_words = load_words()
    max_value = 0
    max_word = ''
    for word in list_words:
        value_word = calc_word_value(word)
        if value_word > max_value:
            max_value = value_word
            max_word = word
    return max_word

if __name__ == "__main__":
    pass # run unittests to validate
