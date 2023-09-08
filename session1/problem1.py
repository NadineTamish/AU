#problem 1
x=int (input("enter height:"))
while x>8 or x<0:
    x=int(input("enter height:"))
for i in range(1,x+1):
    print((x+1-i)*" "+"#"*i+"  "+"#"*i)

