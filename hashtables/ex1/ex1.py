#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_retrieve
                        )


def get_indices_of_item_weights(weights, length, limit):
    # change this to avoid having to resize
    ht = HashTable(16)

    """
    takes in three arguments:
    weights - a list of integers
    length - the length of the list
    limit - the integer to solve for 

    loop through weights and add them to the hash table. key = weight, value = index
    look through weights and check, is limit - weight[i] in the ht?

    ht has linked list functionality so will need to traverse the entries at each index to confirm the above ** retrieve does this for me
    
    What to return? Question reads as - return the first pair that satisfies these conditions, in ascending index order (i.e. whichever comes first in the array)
    """
    for k, v in enumerate(weights):
        hash_table_insert(ht, v, k)
        
    for k, v in enumerate(weights):
        difference = limit - v
        if hash_table_retrieve(ht, difference) is not None:
            
            difference_index = hash_table_retrieve(ht, difference)
            
            if difference_index >= k:
                return [difference_index, k]
            else: 
                return [k, difference_index]
    return None



def print_answer(answer):
    if answer is not None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")
