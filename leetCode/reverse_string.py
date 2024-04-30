def reverse_string(str:str):
    str1 = ""   # Declaring empty string to store the reversed string  
    for i in str:  
        str1 = i + str1  
    return str1    # It will return the reverse string to the caller function  
    # reversed_str = str1[::-1]
    # list1 = [1,2,3,4,5,6,7]
    # print(list1[-1::-1])

    # return reversed_str

result = reverse_string('akello')
print(result)

