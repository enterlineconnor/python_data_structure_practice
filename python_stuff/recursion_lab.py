

import time

from numpy import array

# my_string = '!dlroW olleH'

# def reverse_my_string(my_string, x = 0):

#     current = len(my_string) - 1 - x
#     if current < 0:
#         return ""

#     return my_string[current] + reverse_my_string(my_string,x+1)

# print(reverse_my_string(my_string))


# dec = 192019

# def dec_to_bin(dec, bin_string=''):
#     if dec == 0:
#         return bin_string
    
#     bin_string = str(dec % 2) + str(bin_string)
#     return dec_to_bin(dec // 2, bin_string)

# print(dec_to_bin(dec))



# def factorial_of_num(num):
#     if num <= 1: 
#         return num
#     return num * factorial_of_num(num-1)

# print(factorial_of_num(1000000))


# poly_array = [
#     1,
#     2,
#     5,
#     [2,3,6],
#     6,
#     2,
#     [2, [3, 5, 2] ],
# ]

# basic_array = [1,2,3,[1]]

# only_sub_array = [2,[2,3]]


# def traverse_all(my_array):
#     if len(my_array) == 0:
#         return
#     ele = my_array.pop()
#     if isinstance(ele,list):
#         sub_array = ele
#         traverse_all(sub_array)
#     if isinstance(ele,int):
#         print(ele)

#     traverse_all(my_array)


# traverse_all(poly_array)

# for x in poly_array:
#     if isinstance(x,list):
#         print('LIST')
#     else:
#         print(x)



# base_array = [1,2,3,4,5]

# def double_array(base_array, index=0):
#     if index >= len(base_array):
#         return base_array
#     base_array[index] *= 2
#     return double_array(base_array,index+1)

# print(double_array(base_array))


# def staircase(n):
#     if n == 1 or n == 0: return 1
#     if n < 0: return 0
#     return staircase(n - 1) + staircase(n - 2) + staircase(n - 3)

# for x in range(1,31):
#     print('{}: {}'.format(x,staircase(x)))



# my_array = ['ab','c','def','ghij']


# def unique_letters(my_array, found={}, unique_string = ''):
#     if len(my_array) == 0:
#         return ''
#     ele = my_array.pop()
#     for x in ele:
#         if found.get(x) is None:
#             found[x] = True
#             unique_string += x
#     unique_string += unique_letters(my_array,found)
#     return unique_string

# print(unique_letters(my_array))


# my_array = [1,2,5,4,3,6,8,9]


# def get_even_numbers(my_array,even_array=[]):
#     if len(my_array) == 0:
#         return even_array
#     ele = my_array.pop()
#     if ele % 2 == 0:
#         even_array.append(ele)
#     return get_even_numbers(my_array,even_array)

# print(get_even_numbers(my_array))


# my_arr = [1,2,3,4,6,3,4,1,8,9,0]

# def find_max(my_arr):
#     if len(my_arr) == 1:
#         return my_arr[0]
#     if my_arr[0] > find_max(my_arr[1:]):
#         return my_arr[0]    
#     else:
#         return find_max(my_arr[1:])

# def find_max_b(my_arr):
#     if len(my_arr) == 1:
#         return my_arr[0]
#     x = find_max_b(my_arr[1:])
#     if my_arr[0] > x:
#         return my_arr[0]    
#     else:
#         return x

# print(find_max(my_arr))
# print(find_max_b(my_arr))


# def fib_x(n,memo={}):
#     if n == 0 or n == 1:
#         return n
#     if not memo.get(n):
#         memo[n] = fib_x(n-2,memo) + fib_x(n-1,memo)
#     return memo[n]


# def fib(n):
#     if n == 0 or n == 1:
#         return n
#     return fib(n-2) + fib(n-1)

# start_time = time.time()
# print('First One: {}'.format(fib_x(1994)))
# end_time_x = time.time() - start_time
# # start_time = time.time()
# # print('Second One: {}'.format(fib(40)))
# # end_time_y = time.time() - start_time

# print("Time")
# print("First: {}".format(end_time_x))
# # print("Second: {}".format(end_time_y))




# def add_until_100(array):
#     if len(array) == 0: return 0
#     x = add_until_100(array[1:])
#     if array[0] + x > 100:
#         return x
#     else:
#         return array[0] + x

# def add_until_100_bad(array):
#     if len(array) == 0: return 0
#     if array[0] + add_until_100(array[1:]) > 100:
#         return add_until_100(array[1:])
#     else:
#         return array[0] + add_until_100(array[1:])

# array = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
# print(add_until_100(array))
# print(add_until_100_bad(array))

    


# def golomb(n):
#     if n == 1: return 1 
#     return 1 + golomb(n-golomb(golomb(n-1)))


# def golomb_memo(n,mem={}):
#     if n == 1: return 1 
#     if mem.get(n) is None:
#         mem[n] = 1 + golomb_memo(n-golomb_memo(golomb_memo(n-1,mem),mem),mem)
#     return mem[n]

# print(golomb_memo(100))
# print(golomb(100))
