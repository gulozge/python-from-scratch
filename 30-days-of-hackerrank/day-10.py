import math
import os
import random
import re
import sys


def convert_to_binary(n: int) -> str:
    result = str()
    while n != 0:
        result = result+str(n % 2)
        n = n//2
    result = result[::-1]
    return result


def most_recurring_value(s: str) -> int:
    count = 1
    max_count = 1
    for i in range(0, len(s)-1):
        if s[i] == s[i+1]:
            count = count+1
        else:
            max_count = max(count, max_count)
            count = 1
    max_count = max(max_count, count)
    return max_count


if __name__ == '__main__':
    n = int(input().strip())
    s = convert_to_binary(n)
    print(most_recurring_value(s))
