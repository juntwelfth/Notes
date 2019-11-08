def linear_search(search_list, target_value):
    for idx in range(len(search_list)):
        if search_list[idx] == target_value:
            return idx
    raise ValueError("{0} not in list".format(target_value))


print(linear_search([1, 2, 3, 4, 5], 4))
print(linear_search([1, 3, 5, 7, 9], 10))
