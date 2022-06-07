class BubbleSort:
    def impl(self, arr):
        for i in range(len(arr) - 1, 0, -1):
            print(arr[:i])
            for j in range(i):
                if arr[j] > arr[j + 1]:
                    temp = arr[j]
                    arr[j] = arr[j + 1]
                    arr[j + 1] = temp

        print(arr)


if __name__ == '__main__':
    bbs = BubbleSort()
    bbs.impl([100, 2, 4, 23, 24, 23, 3])
