class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        anagram_map={}

        for word in strs:
            sorted_key = "".join(sorted(word)) # makes dcba -> abcd ie sorts

            if sorted_key not in anagram_map:
                anagram_map[sorted_key]=[]
            
            anagram_map[sorted_key].append(word)
        
        return list(anagram_map.values())


            