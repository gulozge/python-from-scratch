import math
import os
import random
import re
import sys


def is_gmail(emailID):
    return emailID.endswith('@gmail.com')


if __name__ == '__main__':
    N = int(input().strip())
    valid_names = list()
    for N_itr in range(N):
        first_multiple_input = input().rstrip().split()

        firstName = first_multiple_input[0]

        emailID = first_multiple_input[1]

        if is_gmail(emailID):
            valid_names.append(firstName)

    for name in sorted(valid_names):
        print(name)
