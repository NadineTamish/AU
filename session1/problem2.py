import math
x= input("enter text:")
letter=0
sentence=0
word=1
for i in x:
    if i==" ":
        word+=1
    elif i=="." or i=="!":
        sentence+=1
    elif i=="'" or i == ",":
        continue
    else:
        letter+=1
L=letter/word*100
S=sentence/word*100
grade=0.0588 * L - 0.296 * S - 15.8
print("letter=",letter,"sentence=",sentence,"word=",word)
print("grade", grade.__ceil__())