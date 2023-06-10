class Solution:
    def maxValue(self, n: int, index: int, maxSum: int) -> int:
        ret   = 0
        left  = index
        right = n - index - 1

        # Exponential search pt. 1
        lo = 0
        hi = 1
        while True:
            total_sum = (hi + self.__arithmetic_sum(hi - 1, left) +
                self.__arithmetic_sum(hi - 1, right))

            if total_sum > maxSum:
                break
            
            lo = hi
            hi = hi * 2

        # Exponential search pt. 2
        best = 0
        mid  = lo + (hi - lo) // 2
        while lo <= hi:
            total_sum = (mid + self.__arithmetic_sum(mid - 1, left) +
                self.__arithmetic_sum(mid - 1, right))

            if total_sum > maxSum:
                hi = mid - 1
            elif total_sum < maxSum:
                lo   = mid + 1
                best = max(best, mid)
            elif total_sum == maxSum:
                return mid

            mid = lo + (hi - lo) // 2

        return best

    def __arithmetic_sum(self, high_term, slots):
        low_term = max(1, high_term - slots + 1)
        terms    = min(high_term, slots)

        arithmetic_sum = terms * (low_term + high_term) // 2

        return arithmetic_sum + max(slots - high_term, 0)