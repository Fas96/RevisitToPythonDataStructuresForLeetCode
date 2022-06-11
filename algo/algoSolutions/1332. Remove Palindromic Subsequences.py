class LeetCode:
    def rps(self, s):
        subseqls = self.helperfnx(s)

        ls = list(set(subseqls))
        print(ls)
        gls = []
        for i in ls:
            if len(i) > 1:
                gls.append(i)
        pl = self.palindromes(gls)
        countList = self.removePalindrome(s, pl)
        print(countList)
        vals = self.getCount(s, countList)
        print(vals)

    def helperfnx(self, s):
        if len(s) == 0:
            em = []
            return em
        ch = s[0]
        subs = s[1:]
        subss = self.helperfnx(subs)
        res = []
        for val in subss:
            res.append(val)
            res.append(ch.append(val))
        return res

    def palindromes(self, gls):
        pls = []
        for i in gls:
            if i == i[::-1]:
                pls.append(i)
        return pls

    def removePalindrome(self, s, pl):
        res = []
        for i in pl:
            if i in s:
                res.append(i)
        return res

    def getCount(self, s, countList):
        count = 0
        for i in countList:
            if i == s:
                return 1

        return count


def printSubsequences(arr, index, subarr):
    res = []
    if index == len(arr):
        if len(subarr) != 0:
            res.append(subarr)
    else:
        res.append(printSubsequences(arr, index + 1, subarr))
        res.append(printSubsequences(arr, index + 1, subarr + [arr[index]]))

    return res


def helperfnx(s):
    string_ints = [str(int) for int in s]
    s = "".join(string_ints)
    if len(s) == 0:
        em = [""]
        return em
    ch = s[0]
    subs = s[1:]
    subss = helperfnx(subs)
    res = []
    for val in subss:
        res.append(val)
        res.append(ch + val)
    return res


def is2dlist(mylist):
    for item in mylist:
        if isinstance(item, list):
            continue
        else:
            return False
    return True


if __name__ == '__main__':
    nums = [1, 2]
    n = len(nums)
    output = [[]]

    for num in nums:
        output += [curr + [num] for curr in output]
    print([curr for curr in output])
    # td = printSubsequences([1, 2], 0, [])
    # re = []
    # for i in td:
    #     for j in i:
    #         for k in j:
    #             re.append(k)
    # f = []
    # print(is2dlist(re[0]), is2dlist(re[1]))
    # if is2dlist(re[0]):
    #     for k in re:
    #         for m in k:
    #             f.append(m)
    # print([[]] + re)
    # # ltc = LeetCode()
    # # re = helperfnx([-1, 1, 2])
    # # res = []
    # # for r in re:
    # #     if len(r) == 0:
    # #         res.append([])
    # #     else:
    # #         if '-' in r:
    # #             xx = r.replace("-", "")
    # #             print(xx, "--", r, "==")
    # #             xy = [int(x) for x in str(int(xx))]
    # #             res.append()
    # #         else:
    # #             res.append([int(x) for x in str(int(r))])
    # # print(res)
