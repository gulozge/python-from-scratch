class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        min_price = float("inf")
        total_profit = 0

        for price in prices:
            if price < min_price:
                min_price = price

            elif price > min_price:
                total_profit += price-min_price
                min_price = price

        return total_profit


solution = Solution()
print(solution.maxProfit([7, 1, 5, 3, 6, 4]))
