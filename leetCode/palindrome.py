def is_palindrome(str1:str):
    reversed_str = str1[::-1]
    if reversed_str == str1:
        return 'is palindrome'
    else:
        return 'is not palindrome'
    
result = is_palindrome('r')
print(result)