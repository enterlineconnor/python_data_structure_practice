

# check if the smaller array is a subset of the larger array



def subset_check(list_1, list_2, indexed_values = {}):

    if len(list_1) > len(list_2):
        larger_list = list_1
        smaller_list = list_2

    else:
        larger_list = list_2
        smaller_list = list_1

    for ele in larger_list:
        indexed_values[ele] = True

    for i in smaller_list:
        if indexed_values.get(i) is None:
            return False
    return True


list_1 = ['a','b','c','d','e','f']
list_2 = ['b','c','x']

print(subset_check(list_1,list_2))