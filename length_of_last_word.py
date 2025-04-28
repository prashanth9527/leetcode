class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        x=len(s)-1
        y=0
        if " " in s:
            while s[x] ==" ":
                x-=1
            while s[x]!=" ":
                y+=1
                x-=1
            return y
        else:
            return len(s)

        