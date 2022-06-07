class Solution(object):
    def merge(self, nums1, m, nums2, n):
        if m == 0:
            for i in range(n):
                nums1[i] = nums2[i]
        else:
            if (m != 0) and (n != 0):
                for i in range(n - 1, -1, -1):
                    nums1[m+i] = nums2[i]
                nums1.sort()
        return nums1


if __name__ == '__main__':
    sln = Solution()
    print(sln.merge([1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3))
