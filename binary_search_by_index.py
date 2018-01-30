def binary_search(input_array, value):
    first = 0
    last = len(input_array) - 1
    found = False
    while first <= last and not found:
        middle_point = (first + last)//2
        if input_array[middle_point] == value:
            found = True
        else:
            if value < input_array[middle_point]:
                last = middle_point -1
            else: 
                first = middle_point + 1
    return input_array.index(value) if found else -1
