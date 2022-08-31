




my_array = 1,2,3,4,5



def first_duplicate(my_array):
    seen_dict = {}

    for i in my_array:
        if seen_dict.get(i):
            return i
        else:
            seen_dict[i] = True

    return -1


# print(first_duplicate(my_array))

my_set = {1,2,3}

print(my_set.get(1))