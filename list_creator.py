def get_list(dict, string):
    """List generator from a dictionary

    Args:
        dict (dictionary): is the dictionary that you want to get the list from
        string (string): is the key name that you want to get the list from 

    Returns:
        list: returns a list with the values from the key name 
    """
    data = list(map(lambda item: item[string], dict))
    return data

#help(get_list)