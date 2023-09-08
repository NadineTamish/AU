x=input("1:")
y=input("2:")
counter=0
def anagramcheck(x,y,counter):
    for i in range(len(x)):
        for j in range(len(y)):
            if x[i] == y[j]:
                counter += 1
    if counter == len(x):
        print("anagrams")
    else:
        print("not anagrams")


anagramcheck(x,y,counter)