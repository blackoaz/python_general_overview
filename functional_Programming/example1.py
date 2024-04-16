def names_length():
    """
    function that iterates through a list and returns the length of 
    each item in the list.
    """
    result = list(map(len, ['Lily', 'Japheth', 'Lucy', 'Mary']))
    print(result)
names_length()

def square_number():
    """
    a function that takes in a list of numbers and get a 
    square of each number.
    """

    square = list(map(lambda x:x * x, [1,2,3,4,5,6]))

    print(square)

square_number()