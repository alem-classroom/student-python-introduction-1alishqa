def reverse_dict(dict):
    d = {}
    for key in dict.keys():
        tmp = dict[key]
        d[tmp] = key
    return d
    # swap keys and values within dict and return dict

# dict = {'first': '1st', 'second': '2nd'}
# print(reverse_dict(dict))