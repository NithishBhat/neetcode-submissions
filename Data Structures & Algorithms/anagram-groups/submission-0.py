class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        str_dict={}
        for word in strs:
            sort_word=sorted(word)
            if str(sort_word) in str_dict:
                str_dict[str(sort_word)].append(word)
            else:
                str_dict[str(sort_word)]=[word]
            
        return list(str_dict.values())

        