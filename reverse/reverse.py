def reverse(array):
    reversed_array = []
    for element in array:
        reversed_array.insert(0, element)
    return reversed_array