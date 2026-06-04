class Solution:
    def totalWaviness(self, num1, num2):
        total_waviness = 0
        
        for num in range(num1, num2 + 1):
            if num < 100:
                continue
            
            # Convert to string to access digit neighbors easily
            s = str(num)
            n = len(s)
            
            # Check inner digits for peaks and valleys
            for i in range(1, n - 1):
                if s[i] > s[i - 1] and s[i] > s[i + 1]:  # Peak
                    total_waviness += 1
                elif s[i] < s[i - 1] and s[i] < s[i + 1]:  # Valley
                    total_waviness += 1
                    
        return total_waviness