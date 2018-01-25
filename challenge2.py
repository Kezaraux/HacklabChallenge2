def duplicates(str) :
    '''Str -> str
    >>> duplicates("bookkeeper")
    'eko'
    >>> duplicates("java")
    'a'

    :param str: String
    :return: String
    '''
    chars = "abcdefghijklmnopqrstuvwxyz"
    dups = []
    for char in chars:
        count = str.count(char)
        if count > 1:
            dups.append(char)
    ret = ""
    for item in dups:
        ret += item
    return ret


def shuffle(first, second, third):
    '''

    :param first: String
    :param second: String
    :param third: String
    :return: boolean

    >>> shuffle("abc", "def", "aafedc")
    False
    >>> shuffle("ab", "cd", "dacb")
    True
    '''
    len_match = len(first) + len(second) == len(third)
    if (not len_match):
        return False
    count_to_letter = {}
    for char in first:
        count_to_letter[char] = count_to_letter.get(char, 0) + 1
    for char in second:
        count_to_letter[char] = count_to_letter.get(char, 0) + 1
    for char in third:
        if (count_to_letter[char] != third.count(char)):
            return False
    return True

def remove_vowels(list):
    '''

    :param list: list of String
    :return: list: list of String

    >>> list = ["test", "pie", "apple", "bob"]
    >>> remove_vowels(list)
    >>> list
    ['tst', 'p', 'ppl', 'bb']
    '''
    vowels = ["a", "e", "i", "o", "u"]
    #ret = []
    #for string in list:
    for i in range(0, len(list)):
        new_str = ""
        for char in list[i]:
            if char not in vowels:
                new_str += char
        list[i] = new_str
    #return ret


def new_word(a, b):
    '''

    :param a: String
    :param b: String
    :return:

    >>> new_word("windspeaker", "special")
    'windspecial'
    >>> new_word("cat", "rebound")
    ''
    >>> new_word("beansprouts", "unanswered")
    'beanswered'
    '''
    for i in range(0, len(a)):
        for j in range(0, len(b)):
            if a[i] == b[j]:
                if (a[i+1] == b[j+1]) and (a[i+2] == b[j+2]):
                    return a[:i]+b[j:]
    return ""


def word_score(words):
    '''

    :param word: list of String
    :return: list of String

    >>> list = ['abc', 'apple', 'zebra']
    >>> new_list = word_score(list)
    >>> new_list
    ['zebra', 'apple', 'abc']

    >>> list = ['yugioh', 'exodia', 'slifer', 'bonz', 'dragon', 'comz']
    >>> new_list = word_score(list)
    >>> new_list
    ['yugioh', 'slifer', 'dragon', 'exodia', 'bonz', 'comz']
    '''
    count_to_word = {}
    letter_to_score = {'a':1, 'b':2, 'c':3, 'd':4, 'e':5, 'f':6, 'g':7, 'h':8, 'i':9, 'j':10, 'k':11, 'l':12, 'm':13, 'n':14, 'o':15, 'p':16, 'q':17, 'r':18, 's':19, 't':20, 'u':21, 'v':22, 'w':23, 'x':24, 'y':25, 'z':26}
    ret = []
    for word in words:
        score = 0
        bonus = True
        checked_letters = set()
        for char in word:
            if char in checked_letters:
                bonus = False
            else:
                checked_letters.add(char)
            score += letter_to_score[char]
        if bonus:
            score += 10
        count_to_word[word] = count_to_word.get(word, score)
    for k,v in sorted(count_to_word.items(), key=lambda kv: (-kv[1], kv[0]), reverse=False):
        ret.append(k)
    return ret




if __name__ == "__main__":
    duplicates("bookkeeper")
    shuffle("ab", "cd", "dcab")
    list = ["test", "pie", "apple", "bob"]
    remove_vowels(list)
    print(list)