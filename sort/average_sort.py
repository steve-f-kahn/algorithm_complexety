def average_sort(array):
    if len(array) < 2:
        return array
    
    sum = 0
    for number in array:
        sum += number
    pivot = sum//len(array)

    small_array = []
    large_array = []
    for number in array:
        if number <= pivot:
            small_array.append(number)
        else:
            large_array.append(number)
    sorted_small_array = average_sort(small_array)
    sorted_large_array = average_sort(large_array)
    
    return sorted_small_array + sorted_large_array

    