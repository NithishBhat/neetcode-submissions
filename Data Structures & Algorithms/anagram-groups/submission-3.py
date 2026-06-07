class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        str_dict={}
        char_dict={}
        for i in range(len(strs)):
            for char in strs[i]:
                if char in char_dict:
                    char_dict[char]=char_dict[char]+1
                else:
                    char_dict[char]=1

            if frozenset(char_dict.items()) in str_dict:
                str_dict[frozenset(char_dict.items())].append(strs[i])
            else:
                str_dict[frozenset(char_dict.items())]=[strs[i]]
            char_dict={}
            
        return list(str_dict.values())

        