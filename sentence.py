def longestEvenWord(sentence):
    # Write your code here
    a = sentence.split()
    max_length = 0
    word_even = "00"

    for word in a:
        if len(word) % 2 == 0:
            if len(word) > max_length:
                max_length = len(word)
                word_even = word
        
    return word_even


#sentence = "I stills get"
sentence = "I am Roxaana asd"
print(longestEvenWord(sentence))