


my_arr = [1,2,3,2,5]



def brute_force_first_dup(my_arr):
    min_index_of_dup = len(my_arr)+1
    for i in range(len(my_arr)):
        for j in range(len(my_arr)):
            if i != j:
                if my_arr[i] == my_arr[j] and min_index_of_dup > j and  i < j:
                        min_index_of_dup = j
    if min_index_of_dup == len(my_arr)+1:
        return "No Duplicates Found"
    return my_arr[min_index_of_dup]

print(brute_force_first_dup(my_arr))

