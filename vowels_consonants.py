#
# Complete the 'alphabet_filter' function below.
#
# The function is expected to return TWO STRINGS,
# the first containing consonants only, the second containing vowels only, in their original order.
# The function accepts STRING word as parameter.
#

def alphabet_filter(word):
    # Write your code here
    word_vowels = ''
    word_consonants = ''
    vowels = ['a','e','i','o','u']
    for char in word:
        if char in vowels:
            word_vowels += char
        else:
            word_consonants += char
    return word_consonants, word_vowels



print(alphabet_filter("roxana"))