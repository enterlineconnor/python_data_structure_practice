



from ctypes import pointer


# arr = [1,2,3,4,5,0,0,0,6,7,8,9,10]
arr = []
# arr = [1,2,3,4,5,6,7,8,9,10]


def longest_subarray_sum(arr, target):
    if arr is None or arr == []:
        return False
    if len(arr) == 1: 
        if arr[0] == target:
            return [0]
        else:
            return False
    front_pointer,end_pointer = 0,1
    if len(arr) == 2:
        if arr[front_pointer] + arr[end_pointer] == target:
            return [0,1]
        else:
            return False
    
    current_longest_sub, current_val = [0,0], arr[front_pointer] + arr[end_pointer]
    while front_pointer != len(arr) - 2:
        # Setter
        if  current_val == target and end_pointer - front_pointer > current_longest_sub[1] - current_longest_sub[0]:
            current_longest_sub = [front_pointer,end_pointer]


        # Incrementor
        if current_val <= target and end_pointer != len(arr) - 1:
            end_pointer+=1
            current_val += arr[end_pointer]
        
        # Decrementor
        elif current_val > target or end_pointer == len(arr) - 1:
            current_val -= arr[front_pointer]
            front_pointer+=1
    
    if current_longest_sub == [0,0]:
        return False
    return current_longest_sub



print(longest_subarray_sum(arr,15))