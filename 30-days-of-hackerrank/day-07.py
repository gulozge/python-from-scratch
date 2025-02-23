import math
import os
import random
import re
import sys

if __name__ == '__main__':

    n = int(input().strip())
    arr = list(map(int, input().rstrip().split()))
    arr.reverse()
    st = str()
    for i in arr:
        st = st+str(i)+" "
    print(st)
