def binary_search(input_array, value):
    if len(input_array) > 0:
        middle_point = len(input_array)//2
        if input_array[middle_point] == value:
            return 1
        else:
            if value < input_array[middle_point]:
                return binary_search(input_array[:middle_point], value)
            else: 
                return binary_search(input_array[middle_point+1:], value)
    else:
        return -1
