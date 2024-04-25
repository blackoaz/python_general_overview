def greet(name = 'Paulo'):
    """
    a simple function for greeting
    """
    print('Hello World'+ name)

print(greet.__globals__)
print(greet.__closure__)
print(greet.__module__)
print(greet.__defaults__)
print(greet.__code__)
print(greet.__dict__)
print(greet.__kwdefaults__)