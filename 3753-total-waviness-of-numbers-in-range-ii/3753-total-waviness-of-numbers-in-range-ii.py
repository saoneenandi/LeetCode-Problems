class Solution(object):
    def totalWaviness(self, num1, num2):
        """
        :type num1: int
        :type num2: int
        :rtype: int
        """
        def solve(N):
            if N < 100:
                return 0
            
            s = str(N)
            n = len(s)
            
            # memo dictionary: (idx, prev1, prev2, is_less, is_started)
            memo = {}
            
            def dp(idx, prev1, prev2, is_less, is_started):
                # Base case: if we reach the end, we've successfully formed a number
                if idx == n:
                    return 0, 1 if is_started else 0
                
                state = (idx, prev1, prev2, is_less, is_started)
                if state in memo:
                    return memo[state]
                
                limit = 9 if is_less else int(s[idx])
                total_waviness = 0
                total_count = 0
                
                for d in range(limit + 1):
                    next_is_less = is_less or (d < limit)
                    next_is_started = is_started or (d > 0)
                    
                    # Calculate peak/valley contribution
                    contribution = 0
                    if next_is_started and is_started and prev2 != -1:
                        # prev1 is the middle digit being evaluated
                        if prev1 > prev2 and prev1 > d:  # Peak
                            contribution = 1
                        elif prev1 < prev2 and prev1 < d: # Valley
                            contribution = 1
                            
                    # Recursively get waviness and count from subsequent positions
                    sub_waviness, sub_count = dp(
                        idx + 1, 
                        d if next_is_started else -1, 
                        prev1 if next_is_started else -1, 
                        next_is_less, 
                        next_is_started
                    )
                    
                    # Total waviness added by this branch is:
                    # (contribution * amount of valid numbers it creates) + downstream waviness
                    total_waviness += (contribution * sub_count) + sub_waviness
                    total_count += sub_count
                    
                memo[state] = (total_waviness, total_count)
                return memo[state]
            
            return dp(0, -1, -1, False, False)[0]

        return solve(num2) - solve(num1 - 1)