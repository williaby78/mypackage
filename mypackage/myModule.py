def top_n (items, n):
    """
    Return top n items in an array, in descending order
    
    Arguments: 
        items (array): list or array-like objects
        n(int): num of items to return

    Return:
        array: top n items, in descending order

    Examples:
        >>>top_n([8,3,2,7,4], 3)
        []8,7,3]
    """
    for i in range(n):  #keep sorting until we have the top n items
        for j in range(len(items)-1-i):

            if items[j] > items[j+1]:   # if this items is bigger than the next item
                items[j], items[j+1] = items[j+1], items[j]     #swap the two around in order
    
    #get the last two items
    top_n = items[-n:]

    #return in descedning order
    return top_n = items[::-1]