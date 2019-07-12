#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


def get_indices_of_item_weights(weights, length, limit):
    ht = HashTable(16)

    """
    takes in three arguments:
    weights - a list of integers
    length - the length of the list
    limit - the integer to solve for 

    loop through weights and add them to the hash table. weight = key, value = boolean
    look through weights and check, is limit - weight[i] in the ht?

    ht has linked list functionality so will need to traverse the entries at each index to confirm the above

    What to return? Question reads as - return the first pair that satisfies these conditions, in descending order
    

    """

    return None


def print_answer(answer):
    if answer is None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")
