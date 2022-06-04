def maxArea(height) -> None:
    maxSet = 0

    for l in range(len(height)):
        for r in range(len(height) - 1, 0, -1):
            area = (r - l) * min(height[l], height[r])
            maxSet = max(maxSet, area)
    print(maxSet)


def maxAreaWorking(h):
    l, r = 0, len(h) - 1
    res = 0
    while l < r:
        area = (r - l) * min(h[l], h[r])
        res = max(res, area)
        if h[l] < h[r]:
            l += 1
        else:
            r -= 1
    return  res


if __name__ == '__main__':
    print(maxAreaWorking([1, 8, 6, 2, 5, 4, 8, 3, 7]))