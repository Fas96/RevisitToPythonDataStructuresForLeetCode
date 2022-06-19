class Solution(object):
    def areNumbersAscending(self, s):
        strToken = s.split(' ')
        numTok = [int(n) for n in strToken if n.isdigit()]
        res = True

        for n in range(1, len(numTok)):
            if numTok[n - 1] > numTok[n] or numTok[n - 1] == numTok[n]:
                res = False
                break
        return res


if __name__ == '__main__':
    sln = Solution()
    an=sln.areNumbersAscending("sunset is at 7 51 pm overnight lows will be in the low 50 and 60 s")
    print(an)
