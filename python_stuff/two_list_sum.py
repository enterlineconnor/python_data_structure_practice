


#
array_a = [1,5,3,2,6,8]
array_b = [8,3,5,2,9,0,10]
target = 8



def two_list_sum(array_a,array_b,target):
    compliment = {}
    for i in range(len(array_a)):
        ele_comp = target - array_a[i]
        compliment[ele_comp] = True

    for j in range(len(array_b)):
        if compliment.get(array_b[j]):
            return True

    return False


print(two_list_sum(array_a, array_b, target))


