
def anagram(str1, str2):
    s1 = sorted(str1.lower())
    s2 = sorted(str2.lower())
    return s1 == s2

def funWithAnagrams(text):
    #Write your code here
    list_to_remove = []
    n = len(text)
    for i in range(n): 
        for j in range(i + 1, n): 
            if anagram(text[i], text[j]):
                list_to_remove.append(text[j])
    for i in range(len(list_to_remove)):
        text.remove(list_to_remove[i])
    text.sort()
    return text
  
# Driver Code 
if __name__ == "__main__": 
  
    arr = ["maria","aimar","eu","ue"]
    
    print(funWithAnagrams(arr))