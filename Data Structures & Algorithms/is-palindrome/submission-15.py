class Solution:
    def isPalindrome(self, s: str) -> bool:

        lptr=0
       
        string=[]
        
        for i in s:
            if i.isalnum():
                string.append(i)
        s=string
        rptr=len(s)-1

        if lptr==rptr:
            return True
        while lptr<rptr:
            print(rptr)
            if s[lptr].lower()!=s[rptr].lower():
                return False
            lptr=lptr+1
            rptr=rptr-1
        return True
            
