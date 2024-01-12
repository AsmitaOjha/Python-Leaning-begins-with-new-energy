def is_palindrome(string):
    """
    Check if a string is a palindrome.
    A palindrome is a string that reads the same forwards as backwards.
    :param string: The string to check.
    :return: True if 'string' is a palindrome, False otherwise.
    
    """
    return string[::-1].casefold()==string.casefold()
#slicing
#sytax 'start:stop:step'
#when all three parts are empty or unspecified, it defaults to the entire string
#here step = -1 indicates that string should be transversed in reverse order
output = is_palindrome("Madam")
print(output)

def palindrome_sentence(sentence):
    """
    check if a sentence is a palindrome.
    The function ignores whitespace, capitalisation and punctuation in the sentence.
    :param sentence: The sentence to check.
    :return: True if 'sentence' is a palindrome, False otherwise.
    """
    string = ''
    for char in sentence:
        if char.isalnum():
            string +=char
    return is_palindrome(string)
    
result= palindrome_sentence("A Santa lived as a devil at NASA")
print(result)
results=palindrome_sentence("affection for you 🤭")
print(results)