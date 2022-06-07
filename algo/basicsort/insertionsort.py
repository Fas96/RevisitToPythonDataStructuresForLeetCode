class InsertionSort:
    def insertionSort(self, arrs):
        for i in range(1, len(arrs)):
            temp = arrs[i]
            j = i - 1
            while temp < arrs[j] and j > -1:
                arrs[j + 1] = arrs[j]
                arrs[j] = temp
                j -= 1

        print(arrs)


if __name__ == '__main__':
    inss = InsertionSort()
    print(inss.insertionSort([12, 23, 1, 2, 423, 31, 3]))
