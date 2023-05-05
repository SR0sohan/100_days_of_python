import random
#! Take the massage you want to convert to the code
st = input("Please enter: ")
words = st.split(" ")

coding = input("Please enter 1 to code and 2 to decode a massage ")
coding = True if (coding == "1") else False
#? Avobe ^^ this short hand if else condition used to indicate the action
if (coding):
    newWords = []
    for word in words:
        if (len(word)>=3):
            # TO generate random meaningless phrass for the coded massage
            chars = "abcefghijklmopqrsuvwxyz"
            length = 3
            r1 = ""
            r2 =""
            for a in range(length):
             r1 += random.choice(chars)
             r2 += random.choice(chars)
            # Here the genarated random phrases are added to the the actual words.  
            stnew = r1 + word[1:] + word[0] +r2
            newWords.append(stnew)
        else:
            newWords.append(word[::-1])
    print(" ".join(newWords))
else:
    #todo: Else condition to decode the coded massage. Thia function will only word for the avobe coding funcion.It will not respond to any other code functions.
    newWords = []
    for word in words:
        if (len(word)>=3):
            stnew = word [3:-3]
            stnew = stnew[-1] + stnew[:-1]
            newWords.append(stnew)
        else:
            newWords.append(word[::-1])
    print(" ".join(newWords))
        