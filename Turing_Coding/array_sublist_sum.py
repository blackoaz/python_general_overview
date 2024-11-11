def count_divisible_sublists(lst, divisor, limit):
    n = len(lst)
    count = 0
    valid_sublists = []

    # Iterate through all possible sublists with length constraint
    for i in range(n):
        current_sum = 0
        sublist = []
        for j in range(i, min(i+limit, n)):
            sublist.append(lst[j])
            current_sum += lst[j]
            # Check if the current sum is divisible by the divisor
            if current_sum % divisor == 0:
                count += 1
                valid_sublists.append(list(sublist))

    return count, valid_sublists

# Example usage:
lst = [6,9, 6, 6]
divisor = 3
limit = 3
count, valid_sublists = count_divisible_sublists(lst, divisor, limit)
print("Count:", count)
print("Valid sublists:", valid_sublists)
