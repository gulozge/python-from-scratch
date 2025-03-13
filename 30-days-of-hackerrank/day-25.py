import math


class Solution:
    def prime_or_notPrime(number):
        if number <= 1:
            print("Not prime")
            return
        if number == 2:
            print("Prime")
            return

        for i in range(2, int(math.sqrt(number)) + 1):
            if number % i == 0:
                print("Not prime")
                return
        else:
            print("Prime")

    n = int(input())
    for i in range(n):
        number = int(input())
        prime_or_notPrime(number)
