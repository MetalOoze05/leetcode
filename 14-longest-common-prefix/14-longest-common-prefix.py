class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        longest_prefix = ""
        
        if strs is None or len(strs) == 0:
            return longest_prefix

        if len(strs) == 1:
            return strs[0]
            
        first_word = strs[0]
                
        for i in range(0, len(first_word) + 1):
            prefix = first_word[0: i]

            should_update_longest = True
                       
            for another_word in strs[1:]:
                if (another_word[0: i] != prefix):
                    should_update_longest = False
                    break
            
            if should_update_longest:
                longest_prefix = prefix           
            else:
                break

        return longest_prefix