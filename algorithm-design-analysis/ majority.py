class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        n = len(nums)
        threshold = n / 2
        for i in nums:
            if nums.count(i) > threshold:
                return i

nums = [3,2,3]
sol = Solution()
print(sol.majorityElement(nums))