class Difference:
    def __init__(self, a):
        self.__elements = a
        self.maximumDifference = 0

    def computeDifference(self):
        a = self.__elements.copy()
        a.sort()
        self.maximumDifference = abs(a[0] - a[-1])
        return self.maximumDifference


_ = input()
a = [int(e) for e in input().split(' ')]

d = Difference(a)
d.computeDifference()

print(d.maximumDifference)
