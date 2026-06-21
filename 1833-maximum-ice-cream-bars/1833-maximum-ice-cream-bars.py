class Solution(object):
    def maxIceCream(self, costs, coins):
        """
        :type costs: List[int]
        :type coins: int
        :rtype: int
        """
        if not costs:
            return 0
            
        # Step 1: Find the maximum cost to size our counting array
        max_cost = max(costs)
        
        # Step 2: Initialize frequency array
        freq = [0] * (max_cost + 1)
        for cost in costs:
            freq[cost] += 1
            
        total_ice_creams = 0
        
        # Step 3: Greedily buy from the cheapest to the most expensive
        for cost in range(1, max_cost + 1):
            # Skip if there are no ice creams at this price
            if freq[cost] == 0:
                continue
                
            # If we don't have enough coins for even one bar at this price, we're done
            if coins < cost:
                break
                
            # Buy as many as we can afford, or all of them if we have enough coins
            buy_count = min(freq[cost], coins // cost)
            
            # Deduct the cost from our coins and add to our total
            coins -= buy_count * cost
            total_ice_creams += buy_count
            
        return total_ice_creams