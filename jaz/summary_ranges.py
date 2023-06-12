class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums:
            return []

        first, last = nums[0], nums[0]
        intervals   = []
        for num in nums[1:]:
            if num == last + 1:
                last = num
            else:
                intervals.append(f'{first}->{last}' if first != last else f'{first}')
                first, last = num, num

        intervals.append(f'{first}->{last}' if first != last else f'{first}')
        return intervals