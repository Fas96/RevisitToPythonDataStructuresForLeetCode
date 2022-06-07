from functools import reduce
from itertools import permutations


class Solution:
    def reverseString(self, s):
        if len(s) == 0:
            return s
        else:
            return self.reverseString(s[1:]) + s[0]



def reverse_string(my_string):
    if len(my_string) == 0:
        return my_string
    else:
        return reverse_string(my_string[1:]) + my_string[0]


def isContigious(test_list, sublist):
    res = False
    for idx in range(len(test_list) - len(sublist) + 1):
        if test_list[idx: idx + len(sublist)] == sublist:
            res = True
            break
    return res
def longestContiguesSub(ls, k):
    ls = str(ls)
    st = []
    for i in ls:
        st.append(int(i))
    maxM = 0
    res = 0
    for i in range(len(st)):
        listOfList = permutations(st, i)
        for a in listOfList:
            if isContigious(st, list(a)):
                num = 0
                if len(list(a)) == 2:
                    for n in list(a):
                        num += n
                        num *= 10
                    if num != 0:
                        res += 1
                maxM += 1
    return res


if __name__ == '__main__':
    print(longestContiguesSub(430043, 2))
