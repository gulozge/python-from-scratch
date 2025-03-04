import math
import os
import random
import re
import sys


if __name__ == '__main__':
    S = input()
    try:
        print(int(S))
    except ValueError:
        print("Bad String")
