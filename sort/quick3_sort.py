def quick3_sort(array):
    if len(array) < 2:
        return array
    pivot1 = array.pop()
    pivot2 = array.pop()

    if pivot1 < pivot2:
        piv_small = pivot1
        piv_large = pivot2
    else:
        piv_large = pivot1
        piv_small = pivot2

    small_array = []
    medium_array = []
    large_array = []

    for number in array:
        if number < piv_small:
            small_array.append(number)
        elif number < piv_large:
            medium_array.append(number)
        else:
            large_array.append(number)
    
    sorted_small_array = quick3_sort(small_array)
    sorted_medium_array = quick3_sort(medium_array)
    sorted_large_array = quick3_sort(large_array)

    return sorted_small_array + [piv_small] + sorted_medium_array + [piv_large] + sorted_large_array