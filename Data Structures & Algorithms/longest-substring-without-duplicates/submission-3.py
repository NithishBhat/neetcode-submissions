class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        slo_ptr=0
        maxlen=0
        for i in range(1,len(s)):
            if s[i]==s[slo_ptr]:
                maxlen=max(maxlen,i-slo_ptr)
                slo_ptr+=1
                    
        return maxlen
            