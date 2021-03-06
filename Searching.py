# Carlin MacKenzie, 29/08
initArray = [5, 3, 10, 24, 26, 1, 7]

# Insertion
array = list(initArray)
for l in range(1, len(array)):  # traverse once, skip 1st element
    index = l
    value = array[l]
    # while there is space to move to and it is unsorted
    while index > 0 and value < array[index-1]:
        # swap adjacent values
        temp = array[index]
        array[index] = array[index-1]
        array[index-1] = temp
        index -= 1 # move counter down the array
print(array)

# Selection
array = list(initArray)
for k in range(len(array)):  # traverses array once
    minVal = k
    # find min
    for j in range(k+1, len(array)):
        if array[minVal] > array[j]:
            minVal = j
    # swap lowest with current index
    temp = array[k]
    array[k] = array[minVal]
    array[minVal] = temp
print(array)

# Bubble Sort
array = list(initArray)
swap = True
while swap:  # runs until it is sorted
    swap = False  # resets flag
    for i in range(len(array)-1):  # traverses whole array
        if array[i] > array[i+1]:  # if values are unsorted
            swap = True  # triggers flag
            # swaps the unsorted adjacent values
            temp = array[i]
            array[i] = array[i+1]
            array[i+1] = temp
print(array)

# Quick Sort
array = list(initArray)
def quickSort(begin, end):
    pivot = (begin + end) // 2
    for m in range(pivot):
        begin += m
        end -= m
        if array[begin] > array[end]:
            temp = array[begin]
            array[begin] = array[end]
            array[end] = temp

quickSort(0, len(array)-1)
print(array)
print(initArray)
