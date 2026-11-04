class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        
        ptr1=0
        ptr2=0
        long=""
        short=""

        if len(text1)>len(text2):
            long=text1
            short=text2
        else:
            long=text2
            short=text1
        
        while ptr1<len(short) and ptr2 <len(long):
            
            if short[ptr1] == long[ptr2]:
                ptr1=ptr1+1
                ptr2=ptr2+1
            else:
                ptr2=ptr2+1

   
        if ptr1==len(short):
            return len(short)
        
        return 0
            
        
        



