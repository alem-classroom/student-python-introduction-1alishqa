def size_of_set(set):
    return len(set)
    # return size of set  

def is_elem_in_set(set, elem):
    return elem in set
    # return true if elem exists in set, false otherwise

def are_sets_equal(first_set, second_set):
    return first_set == second_set
    # return true if sets have the same elements inside, otherwise false

def add_elem_to_set(set, elem):
    set.add(elem)
    return set
    # add elem to the set if elem does not exist in set, and return the set
    # if elem exists in set, return set

def remove_elem_if_exists(set, elem):
    if is_elem_in_set(set, elem):
        set.remove(elem)

    return set;
    # remove elem from set if it exists, and return the set

def delete_first_element(set):
    x = set.pop()
    return x
    # delete first elemenent of set

# print(size_of_set({1, 2, 3}))
# print(size_of_set({1.0, 'Hello', 3, (1, 2, 3)}), '\n')

# print(is_elem_in_set({15, 20, 'some', 'txt'}, 201))
# print(is_elem_in_set({15, 20, 'some', 'txt'}, 'txt'), '\n')

# print(are_sets_equal({1, 2, 3}, {1, 2, 3}))
# print(are_sets_equal({1, 2, 3}, {15, 20, 'some', 'txt'}), '\n')

# print(add_elem_to_set({1, 2, 3}, 4))
# print(add_elem_to_set({1, 2, 3}, 3), '\n')

# print(remove_elem_if_exists({1, 2, 3}, 3))
# print(remove_elem_if_exists({1, 2, 3}, 5), '\n')

# print(delete_first_element({1, 2, 3}))
# print(delete_first_element({'Balr', 15, 20, 'some', 4, 'txt'}))

# my_set = set([1, 2, 3, 2])
# print(my_set)