class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i in range(len(nums)):
            partner_number = target - nums[i]
            if partner_number in seen:
                return [seen[partner_number], i]
            seen[nums[i]] = i
        return []