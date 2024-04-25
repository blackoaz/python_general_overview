from crypt import methods


class Solution(object):
    def mergeAlternately(self, word1, word2):
        
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        list3 = []
        min_len = min(len(word1), len(word2))
        
        for i in range(min_len):
            list3.append(word1[i])
            list3.append(word2[i])
        list3.extend(word1[min_len:])
        list3.extend(word2[min_len:])
        return ''.join(val for val in list3) 
result = Solution()
print(result.mergeAlternately('ab', 'pqrs'))


"""
class Solution(object):
    def mergeAlternately(self, word1, word2):
        res = ""
        for l1,l2 in zip(word1, word2):
            res+=l1+l2
        diff=len(word1) - len(word2)
        if(diff>0):res+=word1[-diff:]
        elif(diff<0):res+=word2[diff:] 
        return res           
"""