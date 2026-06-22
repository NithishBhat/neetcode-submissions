class Solution:

    def encode(self, strs: List[str]) -> str:
        
        newStr=""
        for i in range(len(strs)):
           newStr=newStr+strs[i]+"*1#checksum#*1"
        return newStr

    def decode(self, s: str) -> List[str]:
        newList=[]
        newList=s.split("*1#checksum#*1")
        return newList[:-1]

