def clear_dict(dict):
    dict.clear()
    return dict
    # delete everything in dict and return it

def get_dict_items(dict):
    return dict.items()
    # return keys and values of dict

def get_dict_keys(dict):
    return dict.keys()
    # return keys of dict

def get_dict_value_by_key(dict, key):
    return dict.get(key)
    # return values of dict that is stored in key

def delete_dict_element_by_key(dict, key):

    for i in dict.keys():
        if i == key:
            dict.pop(key)
            break

    return dict
    # delete and element from dict, such that its key is the argument key

print(clear_dict({"city": "Almaty", "country": "KZ"}), '\n')

print(get_dict_items({"city": "Almaty", "country": "KZ", 'company': 'Samruk'}), '\n')

print(get_dict_keys({'game': 'cheese', 'position': 'forward'}), '\n')

print(get_dict_value_by_key({'game': 'cheese', 'position': 'forward'}, 'position'))
print(get_dict_value_by_key({'goals': 20, 'season': 19}, 'position'), '\n')

print(delete_dict_element_by_key({'goals': 20, 'season': 19}, 'goalsss'))
print(delete_dict_element_by_key({'goals': 20, 'season': 19}, 'goals'))