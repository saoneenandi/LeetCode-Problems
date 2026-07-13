class Solution(object):
    def sequentialDigits(self, low, high):
        """
        :type low: int
        :type high: int
        :rtype: List[int]
        """
        result = []
        queue = deque(range(1, 9)) 
        while queue:
            num = queue.popleft()
            if low <= num <= high:
                result.append(num)
            last_digit = num % 10
            if last_digit < 9:
                next_num = num * 10 + (last_digit + 1)
                if next_num <= high:
                    queue.append(next_num)
        return sorted(result)