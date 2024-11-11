# list1 = ['A', 'B','C','D','E']
# new_list = []


# for item in list1:
#     if item != 'B':
#         new_list.append(item)
#         print(item)
# list1 = new_list

import json


my_data = [{"name":"mike","age":20, "career":"doctor"}]

# for key,val in my_data[0].items():
#     if key == 'name' and val == 'mike':
#         print("Hello", val)

with open ("data.json", "w") as file:
    json.dump(my_data,file, indent=2,sort_keys=True)

with open ("data.json", "r") as file:
    fil = json.load(file)
    print(fil)