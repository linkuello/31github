#def grader (g1 ,g2, g3):
   # avg = (g1 + g2 + g3) / 3
    #result = ""
    #if avg > 95:
    #    result = "A+"
    #elif 85 < avg < 95:
     #   result = 'A'
    #elif 65 < avg < 85:
     #   result = "B"
    #else: 
     #   result = "C"
    #return result
def longest_word(txt):
    maks = 0
    words = txt.split
    for i , v in enumerate(words):
        if len (v) > (words[maks]):
            maks = i
    return words[maks]
print (longest_word ("Hello everybody I hope you are happy today!!!"))
def find_max(arr):
    maxx = arr[0]
    for n in arr :
        if n > maxx:
            maxx > n 
        return maxx 
    
def dublicate_letters (word):
    res = ""
    for i, v in enumerate(word):
        res += (i * 1)    
    print (res)

dublicate_letters("hello")

def duplicate_letters(word):
    res = ""
    for letter in word:
        res += letter * 2
    print(res)

duplicate_letters("hello")

def reversed_words (txt):
    words = txt.split ()
    res = ""
    for i, v in enumerate (words):
        res += "".join(reversed(list(v))) + " "
        return res