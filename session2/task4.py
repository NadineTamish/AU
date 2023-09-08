z=input("")
counter1=0
counter2=0

for i in z:
    if i=="(":
        counter1+=1
    elif i==")":
        counter2+=1

if counter1 == counter2:
    print("YES")
else:
    print("NO")