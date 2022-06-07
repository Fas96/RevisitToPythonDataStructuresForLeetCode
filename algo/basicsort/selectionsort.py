class SelectiveSort:
    def impl(self, arr):
        for i in range(len(arr) - 1):
            mnIdx = i
            for j in range(i + 1, len(arr)):
                if arr[j] < arr[mnIdx]:
                    mnIdx = j
            if i != mnIdx:
                arr[i], arr[mnIdx] = arr[mnIdx], arr[i]
        return arr


if __name__ == '__main__':
    slsort = SelectiveSort()
    print(slsort.impl([3, 1, 3, 2, 12, 42, 4]))
