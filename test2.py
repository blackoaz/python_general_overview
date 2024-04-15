# from array import *

# print(dir(array))


# my_array = array('i', [1,2,3,4,5]) 
# for i in my_array:
#     print(i)

list = [1,2,3,4]
list2 = [5,6,7,8]

list3 = zip(list, list2)
print(list3)
result = enumerate(list3)
print(result)