def duplicate_checker(array):
    for element in array :
        if array.count(element) > 1 : return True
    return False 