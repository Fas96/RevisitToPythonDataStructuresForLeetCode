class Solution(object):
    def cellsInRange(self, s):
        splArr = s.split(":")
        scr = splArr[0]
        scrCol = scr[0]
        scrRow = scr[1]
        ecr = splArr[1]
        ecrCol = ecr[0]
        ecrRow = ecr[1]
        res=[]
        for i in range(ord(scrCol), ord(ecrCol) + 1):
            for j in range(int(scrRow), int(ecrRow) + 1):
                res.append(chr(i) + str(j))
        print(res)
        return res
if __name__ == '__main__':
    sln = Solution()
    sln.cellsInRange("K1:L2")
