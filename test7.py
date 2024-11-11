# my_list = [1,2,3,89,39,10,42]
# my_vals = []
# target = 9
# for k,v in dict(enumerate(my_list)).items():
#      if v - target in my_list:
#         print(v)
#         my_vals.append(k)
# print(my_vals)
import sys


my_params = {
    "name":"michael",
    "school":"my school",
    "age":30
}

def my_data(**my_params):
    for arg in sys.argv:
        print(arg)
my_data()