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
