numbers = [int(n) for n in input().split()]
S=int(input("sum="))
sorted(numbers)
smallest=0
largest=len(numbers)-1

while largest>smallest:
    if numbers[smallest]+numbers[largest]>S:
        largest-=1
    elif numbers[smallest]+numbers[largest]<S:
        smallest+=1
    elif numbers[smallest]+numbers[largest]==S:
        print("Yes",S,"=",numbers[smallest],"+",numbers[largest])
        break
else:
     print("no")
