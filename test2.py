# from array import *

# print(dir(array))


# my_array = array('i', [1,2,3,4,5]) 
# for i in my_array:
#     print(i)

# list = [1,2,3,4]
# list2 = [5,6,7,8]

# list3 = zip(list, list2)
# print(list3)
# result = enumerate(list3)
# print(result)


Users_code = 'L6PDN'
Month_code = 'L6PDN'

result = Users_code == Month_code
print(result)

from datetime import datetime as mytime
import datetime
# print(mytime.date())
# Get the current date
mydate = datetime.date.today()

# Convert the string date to a datetime.date object
seconddate = datetime.datetime.strptime('2024-08-30', '%Y-%m-%d').date()

# Calculate the difference in days
difference = mydate - seconddate

print(difference)

absVal = abs(-1)
print(absVal)
nums = [1,2,3,4,5,6,7,8,9,10]

closest = nums[0]
for x in nums:
    if abs(x) < abs(closest):
        closest = x
print(closest)