def reverse(array):
    reversed_array = []
    i = 1
    while i <= len(array):
        reversed_array.append(array[len(array)-i])
        i += 1
    return reversed_array