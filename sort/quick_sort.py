def quick_sort(array):
    if len(array) < 2:
        return array
    else:
        pivot = array.pop()
        smaller_array = []
        larger_array = []
        for number in array:
            if number <= pivot:
                smaller_array.append(number)
            else:
                larger_array.append(number)
        sorted_smaller_array = quick_sort(smaller_array)
        sorted_larger_array = quick_sort(larger_array)
        
    return sorted_smaller_array + [pivot] + sorted_larger_array