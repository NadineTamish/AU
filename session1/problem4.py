import math
c=0
x=int(input("enter number:"))
z= [int(i) for i in str(x)]
x = [int(i) for i in str(x)]
if len(x)%2==0:
    x.reverse()
for i in range (len(x)):
    if (i%2)!=0:
        if x[i]*2>=10:
            x[i]=x[i]*2
            a,b=divmod(x[i],10)
            # a=x[i]%10
            # print("A=",a)
            # b=x[i]//10
            # print("b=",b)
            x[i]=a+b
        else:
            x[i]= x[i]*2
y=int(math.fsum(x))
if y%10!=0:
    print("INVALID")
else :
    if z[0]==3 and z[1]==4|7:
        print("American Express")
    elif z[0]==5 and z[1]<=5:
        print("Master Card")
    elif z[0]==4:
        print("VISA")
    else:
        print("??")
        #print(y)
    #if i%2==0:
      #  x[i]*2
       # print(x)





#x=input("enter number:")
#A=x.split()
#print(A)


# numofD=len(x)
# sum=0
# x=int(x)
# for i in A :
#     int (x[i])
#     if i%2==0:
#         x=int(x)
#         if x[i]*2>=10:
#             a=x[i]%10
#             b=x[i]//10
#             c=a+b
#         else :
#             sum=sum+int(x[i])*2+c
#     elif i%2!=0:
#         sum=sum+int(x[i])
#
# if sum%10!=0:
#     print("INVALID")
#for i in x:
 #  A.append()