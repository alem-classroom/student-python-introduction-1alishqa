def insert_squares(arr, num):
    for i in range (1, num + 1):
        arr.append(i * i)
    
    return arr
    # add square of numbers from 1 to num to the list named arr and return list

# arr = [1, 2, 3]
# print(insert_squares(arr, 5))