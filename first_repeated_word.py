
def firstRepeatedWord(sentence):
    # Write your code here
    temp = []
    for word in sentence.split():
        if word in temp:
            return word;
        else:
            temp.append(word)
    return 'None'



sentence = "i am only here and i don t get it"
print(firstRepeatedWord(sentence))