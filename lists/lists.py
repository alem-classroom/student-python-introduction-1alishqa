def size_of_list(list):
    return len(list)
    # return size of list

def add_elem_to_list(list, elem):
    list.append(elem)
    return list
    # add elem to list and return the list

def delete_elem_from_list(list, index = -1):

    if index < 0:
        index = len(list) + index

    if (index >= 0) and (index >= len(list)):
        return []

    x = list.pop(index)
    return list

    # delete element from list, such that its index is index
    # if index is invalid, return empty list

def count_elements_in_list(list, x):
    return list.count(x)
    # count elements in the list that are equal to x and return the count

def sort_list(list):
    list.sort()
    return list
    # return sorted list

def reverse(list):
    list.reverse()
    return list
    # return reversed list

print(size_of_list([1, 4, 'cat']))
print(size_of_list([[5, 6], ['gym', 63]]), '\n')

print(add_elem_to_list([1, 2], 3))
print(add_elem_to_list([70, 71, 72, 73], 'seventy four 74'), '\n')

print(delete_elem_from_list([0, 2, 6, 10, 13, 17, 6, 10, 20, 30, 15, 77], 90))
print(delete_elem_from_list([7, 'cat', 9], -2), '\n')

print(count_elements_in_list([5, 7, 15, 7, 5, 5], 5))
print(count_elements_in_list([5, 7, 15, 7, 5, 5], 55), '\n')

print(sort_list([5, 4, 3, 2, 1, 0]))
print(sort_list([15, 16, 17, 18]), '\n')

print(reverse([0, 1, 2, 3, 4, 5]))
print(reverse(['salam', 707, 104, 'aleikum']))