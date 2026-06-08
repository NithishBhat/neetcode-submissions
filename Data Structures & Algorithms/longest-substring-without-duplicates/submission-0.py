class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        s_dict={}
        max_len=0
        for i in range(len(s)):
            
            if s[i] in s_dict:
                
                max_len=max(max_len,len(s_dict))
                s_dict={}
                s_dict[s[i]]=1
            else:
                s_dict[s[i]]=1
        return max_len