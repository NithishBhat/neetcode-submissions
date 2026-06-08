class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        par_dict={"{":"}","]":"[",")":"("}

        if s==[]:
            return True
        for i in s:
            print(stack,i)
            if i=="{" or i=="[" or i=="(":
                stack.append(i)
            elif stack!=[] and i=="}" and stack[-1]!="{" or i=="]" and stack[-1]!="[" or i==")" and stack[-1]!="(":
                return False
            else:
                if stack!=[]:
                    stack.pop()
        return True