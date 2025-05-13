class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        a=[[1],[1,1]]
        if numRows==1:
            return [a[0]]
        if numRows==2:
            return a
        for _ in range(numRows-2):
            dum=[0]+a[-1]+[0]
            res=[]
            for i in range(len(dum)-1):
                res.append(dum[i]+dum[i+1])
            a.append(res)
        return a
