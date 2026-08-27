class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        len_s =len(s)
        len_t =len(t)
        s_dict={}
        t_dict={}

        if len_s!=len_t:
            return False

        for i in range(len_s):
            if s[i] in s_dict :
                s_dict[s[i]] =s_dict[s[i]] +1
            else:
                s_dict[s[i]] = 1
            
            if t[i] in  t_dict:
                t_dict[t[i]] =t_dict[t[i]] +1
            else:
                t_dict[t[i]] = 1

        return s_dict==t_dict