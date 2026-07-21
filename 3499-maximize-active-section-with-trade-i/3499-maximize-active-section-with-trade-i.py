class Solution(object):
    def maxActiveSectionsAfterTrade(self, s):
        """
        :type s: str
        :rtype: int
        """
        initial_ones = s.count('1')
        t = '1' + s + '1'
        zero_blocks = []
        one_blocks = []
        i = 0
        n = len(t)
        while i < n and t[i] == '1':
            i += 1
        while i < n:
            z_start = i
            while i < n and t[i] == '0':
                i += 1
            zero_blocks.append(i - z_start)
            
            if i < n:
                o_start = i
                while i < n and t[i] == '1':
                    i += 1
                if i < n:
                    one_blocks.append(i - o_start)
        if not one_blocks:
            return initial_ones
        m = len(zero_blocks)
        pref_max = [0] * m
        suff_max = [0] * m
        cur = 0
        for j in range(m):
            pref_max[j] = cur
            cur = max(cur, zero_blocks[j])
        cur = 0
        for j in range(m - 1, -1, -1):
            suff_max[j] = cur
            cur = max(cur, zero_blocks[j])
        max_gain = 0
        for i in range(len(one_blocks)):
            a = zero_blocks[i]
            b = zero_blocks[i+1]
            k = one_blocks[i]
            gain1 = a + b
            other_max = max(pref_max[i], suff_max[i+1])
            gain2 = other_max - k
            max_gain = max(max_gain, gain1, gain2)
        return initial_ones + max_gain