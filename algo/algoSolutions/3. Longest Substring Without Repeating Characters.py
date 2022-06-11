from collections import Counter


def an(iterable):
    for element in iterable:
        if element > 1:
            return True
    return False


def subString(s):
    n = len(s)
    res = []
    for i in range(n):
        for a in range(i + 1, n + 1):
            res.append(s[i: a])
    rls = []
    for v in res:
        if not an(Counter(v).values()):
            rls.append(v)
    return  len(max(rls, key=len))


if __name__ == '__main__':
    print(subString("pwwkew"))
