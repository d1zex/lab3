def unique_elements(input_list):
    unique_list = []
    for item in input_list:
        if item not in unique_list:
            unique_list.append(item)
    return unique_list

original_list = [1, 2, 2, 3, 4, 4, 5, 6, 7, 7, 88, 88, 99, 100, 101, 101]
result = unique_elements(original_list)
print(result) 