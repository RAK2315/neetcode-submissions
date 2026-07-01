class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        '''
        METHOD 1
        anagram_map={}

        for word in strs:
            sorted_key = "".join(sorted(word)) # makes dcba -> abcd ie sorts

            if sorted_key not in anagram_map: # initiates a list by default in any new key made
                anagram_map[sorted_key]=[]
            
            anagram_map[sorted_key].append(word)
        
        return list(anagram_map.values())
        '''

        # METHOD 2
        result = {}
        for word in strs:
            count=[0]*26 # initalises list [0,0,0...,0] 26 0's
            for char in word:
                position = ord(char)-ord("a") # "a" acii is 97, so all are subtracted from it
                                              # Eg: b= 98, so 98-97 = 1, b count at index 1
                count[position]+=1
            
            # List cant be made as dict key
            # So we convert to tuple
            tup_count=tuple(count)

            if tup_count not in result: # Initilises list for any new key
                result[tup_count]=[]    # so it becomes {(0,1,0,..,0):[]}
            
            result[tup_count].append(word) # so it becomes {(1,1,0,..,0):[bat]}

        return list(result.values())




            