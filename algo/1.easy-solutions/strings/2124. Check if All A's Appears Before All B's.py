class Solution(object):
    def checkString(self, s):
        aR = []
        bR = []
        for i in range(len(s)):
            if s[i] == 'a':
                aR.append(i)
            if s[i] == 'b':
                bR.append(i)
        print(aR, bR)
        for a in aR:
            for b in bR:
                if a > b:
                    return False
        return True


if __name__ == '__main__':
    sln = Solution()
    print(sln.checkString("ba"))
