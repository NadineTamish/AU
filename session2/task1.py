x=[1,2,3,4,5,6,7,8,9]
target=11
start=0
end =len(x)-1
def binarysearch(array,target,start,end):
    if end>=start:
        middle = (start + end) // 2
        if target == array[middle]:
            return (print("found=", target))
        elif target > array[middle]:
            nstart = middle + 1
            return binarysearch(array, target, nstart, end)
        elif target < array[middle]:
            nend = middle - 1
            return binarysearch(array, target, start, nend)
    else:
        return (print("Not Found"))


binarysearch(x,target,start,end)