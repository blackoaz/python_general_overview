my_list = [4,8,4,7,6,2,3,1]
target = 7
my_dict = {}

for i, num in enumerate(my_list):
    mult = target - num
    if mult in my_dict:
        print([mult,my_list[i]])
    my_dict[num] = i
print(my_dict)