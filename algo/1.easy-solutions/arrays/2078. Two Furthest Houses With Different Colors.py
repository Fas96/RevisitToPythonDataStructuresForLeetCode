class Solution(object):
    def maxDistance(self, colors):
        resource = 0
        for i in range(len(colors)):
            cdf = 0
            for j in range(len(colors)):
                if i != j and colors[i] != colors[j]:
                    cdf = abs(i - j)
            resource = max(resource, cdf)

        print(resource)


if __name__ == '__main__':
    sln = Solution()
    sln.maxDistance([1, 8, 3, 8, 3])
