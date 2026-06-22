class Solution:

    def encode(self, strs: List[str]) -> str:
        
        newStr=""
        for i in range(len(strs)):
           newStr=newStr+strs[i]+" "
        return newStr

    def decode(self, s: str) -> List[str]:
        newList=[]
        newList=s.split(" ")
        return newList[:-1]

