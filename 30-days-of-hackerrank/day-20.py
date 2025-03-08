import math
import os
import random
import re
import sys


def bubble_sort(a):
    numberOfSwaps = 0
    for i in range(0, len(a)):
        for j in range(0, len(a)-1):
            if (a[j] > a[j + 1]):
                a[j], a[j + 1] = a[j + 1], a[j]
                numberOfSwaps = numberOfSwaps+1

        if numberOfSwaps == 0:
            break

    print(f"Array is sorted in {numberOfSwaps} swaps.")
    print(f"First Element: {a[0]}")
    print(f"Last Element: {a[-1]}")


if __name__ == '__main__':
    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    bubble_sort(a)
