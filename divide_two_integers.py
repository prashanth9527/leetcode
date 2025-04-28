class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31
        k=0
        a=abs(dividend)
        b=abs(divisor)
        sign=1
        if dividend == -2**31 and divisor == -1:
            return (2**31) - 1 
        
        if (dividend<0)^(divisor<0):
            sign*=-1

        if b==1:
            return sign*a
        elif a==b:
            return 1*sign
        while a>=b:
            bit=b
            multi=1
            while a>=(bit<<1):
                bit<<=1
                multi<<=1
            a-=bit
            k+=multi
        return k*sign

