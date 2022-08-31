


# given a list of integers, and a target sum, return true or false if the list contains a pair of numbers that sum's to the target


from numpy import integer
from sympy import false, true


sum = 14

integer_list = [1,2,5,20,3,1,2,31,6,8]


# First inclination is to write nested for loop to iterate over the elements nested, which will result in a O(n^2)

# If we sort the array, which takes O(n) time, we can then write a search to compare the first and last element of the array.
# If the sum of those integers is smaller than the target, we increase the base (lowest). If the sum of those integers is
# larger than our target, we decrease our ceiling (highest). This will result in, worst case scenario, A complete iteration through each
# element, which gives a total of O(2n), which can be truncated to O(n) since constants are removed from Big O notation

# Since our sum is only reached when we get to 20+30, this should be our "worst case" speed, so this should take exactly O(2n) iterations


def sum_has_pair(integer_list, sum):
    integer_list.sort()
    smallest = 0
    largest = len(integer_list) - 1

    while integer_list[smallest] <= integer_list[largest]:
        if integer_list[smallest] + integer_list[largest] == sum:
            print(integer_list[smallest], integer_list[largest])
            return True
        elif integer_list[smallest] + integer_list[largest] < sum:
            smallest += 1
        elif integer_list[smallest] + integer_list[largest] > sum:
            largest -= 1

    return False

def sum_has_pair_set(integer_list,sum,visited=set()):
    for integer in integer_list:
        compliment = sum - integer
        if compliment in visited:
            print('{} + {} = {}'.format(integer,compliment,sum))
            return true
        visited.add(integer)
    return false


print(sum_has_pair(integer_list, sum))

print(sum_has_pair_set(integer_list,sum))
