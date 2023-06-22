import functools

class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        @cache
        def max_move(day, curr_stocks):
            if day >= len(prices):
                return 0

            moves = []
            # BUY
            if not curr_stocks:
                moves.append(max_move(day + 1, 1) - prices[day])
            # SELL
            else:
                moves.append(max_move(day + 1, 0) + prices[day] - fee)
            # HODL
            moves.append(max_move(day + 1, curr_stocks))

            return max(moves)

        return max_move(0, 0)