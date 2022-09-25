def quicksort(arr):
    length = len(arr)
    if length <= 1:
        return arr
    pivot = arr.pop()
    greater = []
    less = []
    for number in arr:
        if number > pivot:
            greater.append(number)
        else:
            less.append(number)
    return(quicksort(less)+[pivot]+quicksort((greater)))
print(quicksort([1,5,7,8,4,3,6,8,9,5,4,2,6,8,9]))