# count = 0
# def fib(n):
#     global count 
#     count += 1 
#     if n <= 2:
#         return 1
#     return fib(n-1) + fib(n-2)

# my_fib = fib(10)
# print(f'Number of iterations:{count}')
# print(my_fib)

def fib2(n):
    list1 = []
    i = 2
    list1.append(0) 
    list1.append(1)

    while i <= n:
        sum = list1[i-1] + list1[i - 2]
        list1.append(sum)
        i  += 1
    print(list1)
    print(i)
    return sum
result = fib2(100)
print(result) 
