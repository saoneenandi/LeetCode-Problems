from bisect import bisect_left, bisect_right

class Solution(object):
    def sumAndMultiply(self, s, queries):
        """
        :type s: str
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        MOD = 10**9 + 7
        m = len(s)
        
        # 1. Precompute standard digit prefix sums for the entire string
        digit_sum = [0] * (m + 1)
        for i in xrange(m):
            digit_sum[i + 1] = digit_sum[i] + int(s[i])
            
        # 2. Identify non-zero digits and track their original indices
        nz_indices = []
        P = [0]  # Prefix value array for rolling hash math
        
        for i in xrange(m):
            if s[i] != '0':
                nz_indices.append(i)
                next_val = (P[-1] * 10 + int(s[i])) % MOD
                P.append(next_val)
                
        N = len(nz_indices)
        
        # 3. Precompute powers of 10
        power10 = [1] * (N + 1)
        for i in xrange(1, N + 1):
            power10[i] = (power10[i - 1] * 10) % MOD
            
        answer = []
        
        # 4. Process each query
        for q in queries:
            l, r = q[0], q[1]
            
            # Use binary search to find relevant non-zero indices within [l, r]
            i = bisect_left(nz_indices, l)
            j = bisect_right(nz_indices, r) - 1
            
            # If no non-zero digits fall in the range
            if i > j:
                answer.append(0)
                continue
                
            # Extract x % MOD using the prefix values
            length = j - i + 1
            x = (P[j + 1] - (P[i] * power10[length]) % MOD) % MOD
            
            # Extract total digit sum in range [l, r]
            sum_val = digit_sum[r + 1] - digit_sum[l]
            
            # Calculate final query answer
            current_ans = (x * (sum_val % MOD)) % MOD
            answer.append(current_ans)
            
        return answer