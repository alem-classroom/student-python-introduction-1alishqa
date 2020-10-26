def size_of_list(list):
    return len(list)
    # return size of list

def add_elem_to_list(list, elem):
    list.append(elem)
    return list
    # add elem to list and return the list

def delete_elem_from_list(list, index = -1):
    empty = []
    if index < 0 or index >= size_of_list(list):
        return empty
    
    list.pop(index)
    return list
    # delete element from list, such that its index is index
    # if index is invalid, return empty list

def count_elements_in_list(list, x):
    count = 0
    for i in list:
        if i == x:
            count = count + 1
    
    return count
    # count elements in the list that are equal to x and return the count

def sort_list(list):
    list.sort()
    return list
    # return sorted list

def reverse(list):
    list.reverse()
    return list
    # return reversed list

# print(size_of_list([1, 4]))
# print(add_elem_to_list([1, 2], 3))
# print(delete_elem_from_list([7, 'cat', 9], 0))
# print(delete_elem_from_list([7, 'cat', 9]))
# print(count_elements_in_list([5, 7, 15, 7, 5, 5], 5))
# print(sort_list([5, 4, 3, 2, 1, 0]))
# print(reverse([0, 1, 2, 3, 4, 5]))