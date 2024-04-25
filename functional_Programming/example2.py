from functools import reduce
from operator import add


names = ['Mary', 'Isla', 'Sam']

result = list(map(lambda x: hash(x), names))

print(result)

sum = reduce(lambda a,x: a + x, [0,1,2,3,4])

print(sum)

filter_list = list(filter(lambda x: x % 2 == 0, [1,2,3,4,5,6,7,8,9,10]))
print(filter_list)

people = [{'name': 'Mary', 'height': 160},
    {'name': 'Isla', 'height': 80},
    {'name': 'Sam'}]

height_total = 0
height_count = 0
for person in people:
    if 'height' in person:
        height_total += person['height']
        height_count += 1

if height_count > 0:
    average_height = height_total / height_count

height_value = list(map(lambda x:x['height'], filter(lambda x: 'height' in x,person)))
if len(height_value) > 0:
    reduced_value = reduce(add,height_value) / len(height_value)
    print('reduced height:',reduced_value)


print ('looped height:',average_height)
# => 120











