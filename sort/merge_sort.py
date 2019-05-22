def merge_sort(array):
    l = len(array)
    if l < 2:
        return array
    else:
        left = array[:l//2]
        right = array[l//2:]
        sorted_left = merge_sort(left)
        sorted_right = merge_sort(right)
    
    i = 0
    j = 0
    result = []
    while i < len(sorted_left) and j < len(sorted_right):
        if sorted_left[i] < sorted_right[j]:
            result.append(sorted_left[i])
            i+= 1
        else:
            result.append(sorted_right[j])
            j+= 1

    while j < len(sorted_right):
        result.append(sorted_right[j])
        j += 1
    while i < len(sorted_left):
        result.append(sorted_left[i])
        i += 1
    
    return result