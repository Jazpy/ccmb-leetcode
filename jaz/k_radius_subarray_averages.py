from collections import deque

class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        ret = [None] * len(nums)
        win  = None
        wsum = None
        
        for i in range(len(nums)):
            if i < k or i >= len(nums) - k:
                ret[i] = -1
                continue

            if not win or not wsum:
                win  = deque(nums[i - k : i + k + 1])
                wsum = sum(win)
            else:
                wsum -= win[0]
                win.popleft()
                win.append(nums[i + k])
                wsum += win[-1]

            ret[i] = wsum // ((k * 2) + 1)

        return ret