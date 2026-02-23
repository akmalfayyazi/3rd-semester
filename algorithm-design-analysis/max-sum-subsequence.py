class Solution:
    def __init__(self):
        self.result = []
        
    def max_subsequence(self, nums):
        if not nums:
            return 0
        if len(nums) == 1:
            return self.result.append(max(0, nums[0]))
        
        dp = [0] * len(nums)
        dp[0] = max(0, nums[0])
        dp[1] = max(dp[0], nums[1])

        for i in range(2, len(nums)):
            dp[i] = max(nums[i] + dp[i-2], dp[i-1])
        
        self.result.append(dp[-1])
    
    def maximumSumSubsequence(self, nums: list[int], queries: list[list[int]]) -> int:
        MOD = 10**9 + 7
        for i, j in queries:
            nums[i] = j
            self.max_subsequence(nums)
        return sum(self.result) % MOD

nums = [3,5,9]
queries = [[1,-2],[0,-3]]
solution = Solution()
print(solution.maximumSumSubsequence(nums, queries))