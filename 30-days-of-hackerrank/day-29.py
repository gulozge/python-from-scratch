import math
import os
import random
import re
import sys


def bitwiseAnd(N, K):
    max_and = -1
    for i in range(1, N):
        for j in range(i+1, N+1):
            current_and = i & j
            if current_and < K and current_and > max_and:
                max_and = current_and
    return max_and


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()

        count = int(first_multiple_input[0])

        lim = int(first_multiple_input[1])

        res = bitwiseAnd(count, lim)

        fptr.write(str(res) + '\n')

    fptr.close()
