from collections import Counter


class Solution(object):
    def kthDistinct(self, arr, k):
        darr = Counter(arr)
        res = []
        for a, v in darr.items():
            if v == 1:
                res.append(a)
        output=res[k - 1] if len(res) >= k else " "

        return output


if __name__ == '__main__':
    sln = Solution()
    print(sln.kthDistinct(["d", "b", "c", "b", "c", "a"], 2))
