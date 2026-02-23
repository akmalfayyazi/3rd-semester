import math

class Solution:
    def euclidean_distance(self, origin, points):
        result = [0] * len(points)
        for i in range(len(points)):
            x, y = points[i]
            dist = math.sqrt((x - origin[0])**2 + (y - origin[1])**2)
            result[i] = dist
        return result

    def kClosest(self, points: list[list[int]], k: int) -> list[list[int]]:
        origin = [0,0]
        result = self.euclidean_distance(origin, points)
        index = sorted(range(len(result)), key=lambda x: result[x])[:k]
        result1 = []
        for i in index:
            result1.append(points[i])
        return result1

points = [[1,3],[-2,2]]
k = 1
solution = Solution()
print(solution.kClosest(points, k))