class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        par_dict={"}":"{","]":"[",")":"("}

        for i in s:
            if i in par_dict and stack!=[] and stack[-1]==par_dict[i]:
                stack.pop()
            elif i in par_dict :
                return False
            else:
                stack.append(i)

        if stack!=[]:
            return False
        return True