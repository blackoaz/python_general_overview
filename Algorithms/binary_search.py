# def binary_search(target):
#     list1 = [x for x in range(1,101)]
    
#     upper_bound = len(list1)-1
#     #print(upper_bound)
#     lower_bound = 0
#     while lower_bound <= upper_bound:
#         mid_point = (upper_bound + lower_bound) // 2
#         print(mid_point)
#         if target == list1[mid_point]:
#             return 'found'
#         elif target > list1[mid_point]:
#             lower_bound = mid_point + 1
#         elif target < list1[mid_point]:
#             upper_bound = mid_point - 1
        
#     return 'Not found'

# print(binary_search(49))
import logging

logging.basicConfig(level=logging.DEBUG)

def binary_search(target, list1):
    upper_bound = len(list1) - 1
    lower_bound = 0
    
    while lower_bound <= upper_bound:
        mid_point = (upper_bound + lower_bound) // 2
        logging.debug(f'Lower bound: {lower_bound}, Upper bound: {upper_bound}, Mid point: {mid_point}')
        
        if target == list1[mid_point]:
            return mid_point
        elif target > list1[mid_point]:
            lower_bound = mid_point + 1
        else:
            upper_bound = mid_point - 1
    
    return -1

# Example usage:
list1 = [x for x in range(1, 101)]
result = binary_search(50, list1)
if result != -1:
    print(f'Target found at index {result}')
else:
    print('Target not found')
