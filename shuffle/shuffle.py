import random

def shuffle(array, seed=None):
    random.seed(a=seed)
    output_array = []
    while len(array) > 0:
        output_array.insert(0,array.pop(random.randint(0,len(array)-1)))
    return output_array
    