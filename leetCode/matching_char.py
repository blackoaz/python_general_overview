def match_char(str1:str,str2:str):
    combined_str = str1 + str2
    print(combined_str)
    list_char = []
    repeated_char = []
    count = 0
    for i in range(len(combined_str)):
        
        if combined_str[i] in list_char:
            repeated_char.append(combined_str[i])
        else:
            count += 1
            list_char.append(combined_str[i])
    return len(repeated_char)

result = match_char('paulo', 'oduor')
print(result)