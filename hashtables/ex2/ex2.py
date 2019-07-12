#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    hashtable = HashTable(length)
    route = [None] * length
    print('WHAT IS ROUTE', type(route))

    """
    YOUR CODE HERE
    Take a list of Tickets
    """
    #  Get the tickets into the HT, key = source and val = destination
    for i in tickets:
        if i.source is "NONE":  # i know this is risky but .upper() was throwing an error and i need to move to blockchain
            hash_table_insert(hashtable, "home", i.destination)
        else:
            hash_table_insert(hashtable, i.source, i.destination)

    start = "home"

    for i in range(0, len(route)):
        dest = hash_table_retrieve(hashtable, start)

        route[i] = dest
        start = dest

    return route
