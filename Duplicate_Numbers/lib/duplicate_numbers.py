def check_dupes(array):
    output = []
    for element in array :
        if array.count(element) >= 2 and output.count(element) == 0 and isinstance(element, int) and not isinstance(element, bool):
            output.append(element)
    return output
    