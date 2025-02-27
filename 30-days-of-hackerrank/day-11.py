import math
import os
import random
import re
import sys


def max_hourglass_sum(arr):
    max_sum = -float('inf')

    for i in range(len(arr) - 2):
        for j in range(len(arr[i]) - 2):
            top = arr[i][j] + arr[i][j+1] + arr[i][j+2]
            mid = arr[i+1][j+1]
            bot = arr[i+2][j] + arr[i+2][j+1] + arr[i+2][j+2]

            hourglass_sum = top + mid + bot

            if hourglass_sum > max_sum:
                max_sum = hourglass_sum

    return max_sum


if __name__ == '__main__':

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))
    print(max_hourglass_sum(arr))
