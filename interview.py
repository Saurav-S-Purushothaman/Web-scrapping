# [3,2,2,3] -> [_, 2, 2, _]

"""optimised code"""


def remove_num_from_array(arr,number,replacement):
    n = len(arr)
    if number not in arr:  
        return arr
    else: 
        for i in range(n): 
            if arr[i] == number: 
                arr[i] = replacement  
    # play around with arr to sort the items 
     

