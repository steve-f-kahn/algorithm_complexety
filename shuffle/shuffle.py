import random

def shuffle(array, seed=None):
    random.seed(a=seed)
    output_array = []
    while len(array) > 0:
        random_index = random.randint(0,len(array)-1)
        output_array.append(array[random_index])
        array[random_index] = array[len(array)-1]
        array.pop()
    return output_array