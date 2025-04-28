from typing import List

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        i=len(digits)-1
        p=0
        for l in digits:
            p=(p*10)+l

        r=[]
        p+=1
        for k in str(p):
            r.append(int(k))
        return r

        
