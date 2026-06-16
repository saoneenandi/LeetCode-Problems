class Solution(object):
    def processStr(self, s):
        """
        :type s: str
        :rtype: str
        """
        result = []
        
        for char in s:
            if char.islower():
                # Append lowercase letter
                result.append(char)
            elif char == '*':
                # Remove the last character if it exists
                if result:
                    result.pop()
            elif char == '#':
                # Duplicate the current result
                result = result + result
            elif char == '%':
                # Reverse the current result
                result.reverse()
                
        return "".join(result)