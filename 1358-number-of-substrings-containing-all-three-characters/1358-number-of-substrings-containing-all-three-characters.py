class Solution(object):
    def numberOfSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        last_seen = {'a': -1, 'b': -1, 'c': -1}
        count = 0
        
        for i, char in enumerate(s):
            # Update the latest position of the current character
            last_seen[char] = i
            
            # The start of the valid substring can be anywhere from 
            # index 0 up to the minimum index of the three characters
            min_idx = min(last_seen['a'], last_seen['b'], last_seen['c'])
            
            # If min_idx is -1, it means we haven't seen all three yet
            if min_idx != -1:
                count += min_idx + 1
                
        return count