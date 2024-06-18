from typing import List
def solution(x:int, y:int, z:List[List[int]]):
        list1 = []
        for i in range(len(z)):
            if z[i][0] == x or z[i][1] == y:
                print('z:',z[i][0] , '==', x , 'and', 'z:',z[i][1] , '==', y)
                #print(i)
                list1.append(i) 
                return i      
        # if list1: 
        #     return list1 
        # else: return -1  
        return -1

result = solution(1, 0, [[0, 1], [0, 4], [0, 6], [7, 8]])
print(result) 

def matrix():
    array1 = [
        [1, 2, 3, 4, 5],
        [6, 7, 8, 9, 10],
        [11,12,13,14,15],
        [16,17,18,19,20]
    ]
    list1 = []
    for i in range(len(array1)):
        print(i)
        for j in range(len(array1[i])):
            if array1[i][j]  % 2 == 0:
                list1.append(array1[i][j])
    return list1
# matrix_result = matrix()
# print(matrix_result)