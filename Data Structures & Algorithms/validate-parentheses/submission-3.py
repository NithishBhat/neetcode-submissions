class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        for i in s:
            if i =="}" and stack!=[] and  stack[-1]=="{":
                stack.pop()
            elif i=="]" and stack!=[] and stack[-1]=="[":
                stack.pop()
            elif i==")" and stack!=[] and stack[-1]=="(":
                stack.pop()
            elif i=="{" or i=="[" or i =="(":
                stack.append(i)
            else:
                return False
            
        if stack!=[]:
            return False
        
        return True