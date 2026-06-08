class Solution:
    def isPalindrome(self, s: str) -> bool:

        lptr=0
        rptr=len(s)-1
        string=[]
        
        for i in s:
            if i.isalnum():
                string.append(i)


        if lptr==rptr:
            return True
        while lptr<=int(len(s)/2) and lptr<rptr:
            while not(s[lptr].isalnum()) and lptr<rptr:
                lptr=lptr+1
            while not(s[rptr].isalnum()) and lptr<rptr :
                rptr=rptr-1


            if s[lptr].lower()!=s[rptr].lower():
                return False
            lptr=lptr+1
            rptr=rptr-1
        return True
            
