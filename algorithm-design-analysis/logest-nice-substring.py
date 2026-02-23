class Solution:
    def is_nice(self, substring):
        result = []
        for i in substring:
            for c in i:
                if c.lower() not in i or c.upper() not in i:
                    break
            else:
                result.append(i)
        length = [0]*len(result)
        for i in range(len(result)):
            length[i] = len(result[i])
        for i in range(len(length)):
            if length[i] == max(length):
                return result[i]
                
    def longestNiceSubstring(self, s: str) -> str:
        length = len(s)
        substring = []
        for j in range(2, length + 1):
            i = 0
            while j - i >= 2:
                substring.append(s[i:j])
                i += 1
        result = self.is_nice(substring)
        return result if result else ""

s = "abABB" 
solution = Solution()
print(solution.longestNiceSubstring(s))