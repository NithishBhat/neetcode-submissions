class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s)==0:
            return 0
        if len(s)==1:
            return 1
        s_dict={s[0]:1}
        sptr=0
        maxlen=0
        for i in range(1,len(s)):
            if s[i] in s_dict:
                print(s_dict)
                while s[i] in s_dict:
                    del s_dict[s[sptr]]
                    sptr=sptr+1
                s_dict[s[i]]=1
            else:
                s_dict[s[i]]=1
            maxlen=max(maxlen,len(s_dict)) 
        return maxlen