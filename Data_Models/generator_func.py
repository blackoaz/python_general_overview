import itertools
def gen():
    yield from 'Hello there'
    # yield 'My name is Paulo'
    # yield 'I love Programming'

result = gen()
for i in result:
    if i == ' ':
        continue
    print(i)
#print(result.__next__())
# print(dir(itertools))
