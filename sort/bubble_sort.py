def bubble_sort(array):
    i = 0
    while i < len(array) - 1:
        if array[i] > array[i+1]:
            array[i], array[i+1] = array[i+1], array[i]
            i = 0
        else:
            i += 1
    return array 