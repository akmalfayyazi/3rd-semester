class Solution:
    def maximumSumSubsequence(self, nums: list[int], queries: list[list[int]]) -> int:
        n = len(nums)
        tree = [ (0, 0, 0, 0) ] * (4*n)

        def merge(left_child, right_child):
            l00, l01, l10, l11 = left_child
            r00, r01, r10, r11 = right_child
            
            s00 = max(l00 + r00, l00 + r10, l01 + r00)
            s01 = max(l00 + r01, l00 + r11, l01 + r01)
            s10 = max(l10 + r00, l10 + r10, l11 + r00)
            s11 = max(l10 + r01, l10 + r11, l11 + r01)
            
            return (s00, s01, s10, s11)

        def build(node, start, end):
            if start == end:
                val = max(0, nums[start])
                tree[node] = (0, 0, 0, val)
                return
            
            mid = (start + end) // 2
            build(2 * node, start, mid)
            build(2 * node + 1, mid + 1, end)
            tree[node] = merge(tree[2 * node], tree[2 * node + 1])

        def update(node, start, end, idx, val):
            if start == end:
                new_val = max(0, val)
                tree[node] = (0, 0, 0, new_val)
                return
            
            mid = (start + end) // 2
            if start <= idx <= mid:
                update(2 * node, start, mid, idx, val)
            else:
                update(2 * node + 1, mid + 1, end, idx, val)
            
            tree[node] = merge(tree[2 * node], tree[2 * node + 1])

        build(1, 0, n - 1)
        
        total_sum = 0
        MOD = 10**9 + 7
        
        for i, j in queries:
            update(1, 0, n - 1, i, j)
            root_node = tree[1]
            current_max = max(root_node)
            total_sum = (total_sum + current_max) % MOD
            
        return total_sum

nums = [3,5,9]
queries = [[1,-2],[0,-3]]
solution = Solution()
print(solution.maximumSumSubsequence(nums, queries))