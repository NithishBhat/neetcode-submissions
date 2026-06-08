class Solution:
    def isPalindrome(self, s: str) -> bool:

        lptr=0
        rptr=len(s)-1
        
        if lptr==rptr:
            return True
        while lptr<=int(len(s)/2) or not(lptr>=rptr):
            while not(s[lptr].isalpha()):
                lptr=lptr+1
            while not(s[rptr].isalpha()) :
                rptr=rptr-1

            print(s[lptr],s[rptr])
            if s[lptr].lower()!=s[rptr].lower():
                return False
            lptr=lptr+1
            rptr=rptr-1
        return True
            
