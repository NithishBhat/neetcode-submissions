class Solution:
    def climbStairs(self, n: int) -> int:
        if n==1 or n==0 or n==2:
            return n
        num1=1
        num2=2
        temp=0
        for i in range(3,n+1):
            temp=num1+num2
            num1=num2
            num2=temp
        return temp