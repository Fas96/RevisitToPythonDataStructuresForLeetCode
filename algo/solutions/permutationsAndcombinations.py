import sys

input = sys.stdin.readline
from collections import deque
import copy
import itertools
from itertools import product
from itertools import permutations, combinations
from itertools import combinations_with_replacement
# from itertools import accumulate
import operator
import random
import string


def first_order(p, q, initial_val):
    """Return sequence defined by s(n) = p * s(n-1) + q."""
    return itertools.accumulate(itertools.repeat(initial_val), lambda s, _: p * s + q)


def second_order(p, q, r, initial_values):
    """Return sequence defined by s(n) = p * s(n-1) + q * s(n-2) + r."""
    intermediate = itertools.accumulate(
        itertools.repeat(initial_values),
        lambda s, _: (s[1], p * s[1] + q * s[0] + r)
    )
    return map(lambda x: x[0], intermediate)


def main():
    num = int(input())
    arr = list(map(int, input().split()))

    if num < 3:
        print("NO")
    elif num == 3:
        arr.sort()
        if arr[0] == arr[1] or arr[1] == arr[2]:
            print("NO")
        else:
            print("YES")
    else:
        checkarr = list(itertools.combinations(arr, 3))
        for s in checkarr:
            tmp = list(s)
            tmp.sort()
            if tmp[0] == tmp[1] or tmp[1] == tmp[2]:
                continue
            else:
                print("YES")
                return
        print("NO")


def accumulate(inputs, func):
    itr = iter(inputs)
    prev = next(itr)
    for cur in itr:
        yield prev
        prev = func(prev, cur)


def fib():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


def naive_grouper(inputs, n):
    num_groups = len(inputs) // n
    return [tuple(inputs[i * n:(i + 1) * n]) for i in range(num_groups)]


def grouper(inputs, n, fillvalue=None):
    iters = [iter(inputs)] * n
    return itertools.zip_longest(*iters, fillvalue=fillvalue)


'''permutation
each of several possible ways in which a set or number of things can be ordered or arranged.

a combination is a selection of items from a set that has distinct members, such that the order of selection does not matter (unlike permutations). 
'''
if __name__ == '__main__':
    print(list(permutations([1, 1, 2], 3)))
    print(set(list(permutations([1, 1, 2], 3))))
    lsi = []
    for ls in set(list(permutations([1, 1, 2], 3))):
        lsi.append(list(ls))
    print(lsi)

    # print(list(combinations_with_replacement([5, 6, 10], 3)))
    # print(list(permutations(['a', 'b', 'c', 'd'], 3)))
    # print(list(product([1, 2], [3, 4], repeat=2)))
    # print(list(permutations([1, 2, 3])))
    #
    # print(list(permutations([5, 6, 10], 3)))
    # print(list(accumulate([1, 2, 3, 2, 2, 2, 2, 2], lambda x, y: (x + y) / 2)))
    # print(list(map(sum, zip([1, 2, 3], [4, 5, 6]))))
    #
    # print(naive_grouper([1, 2, 3, 4, 5, 6], 3))
    # print(list(itertools.islice('ABCDEFG', 2, 5)))
    # print(list(itertools.chain('ABC', 'DEF')))
    # print(list(itertools.chain.from_iterable([[1, 2, 3], [4, 5, 6]])))
    # print(list(itertools.takewhile(lambda x: x < 3, [0, 1, 2, 3, 4])))
    # print(list(itertools.dropwhile(lambda x: x < 3, [0, 1, 2, 3, 4])))
    # print(list(itertools.takewhile(lambda x: x >= 2, [1, 1, 1, 0, 0])))
    # print(list(map(len, ['abc', 'de', 'fghi'])))
    #
    # main()
