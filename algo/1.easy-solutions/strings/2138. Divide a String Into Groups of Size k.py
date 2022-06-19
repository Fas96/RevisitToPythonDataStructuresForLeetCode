class Solution(object):
    def divideString(self, s, k, fill):
        rs = [s[i:i + 3] for i in range(0, len(s), 3)]
        if len(rs[-1]) != k:
            st = fill * (k - len(rs[-1]))
            rs[-1] += st
        return rs


if __name__ == '__main__':
    sln = Solution()
    print(sln.divideString("abcdefghi", 3, "x"))
