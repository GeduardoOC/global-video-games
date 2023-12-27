def get_list(dict, string):
    data = list(map(lambda item: item[string], dict))
    return data