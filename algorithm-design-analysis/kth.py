class Solution:
    def kthLargestNumber(self, nums: list[str], k: int) -> str:
        nums.sort(key=lambda x: (len(x), x))
        return nums[-k]
    
nums = ["2","21","12","1"]
k = 3
sol = Solution()
print(sol.kthLargestNumber(nums, k))