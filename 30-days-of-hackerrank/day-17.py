class Calculator:

    def power(self, num1, num2):
        if num1 < 0 or num2 < 0:
            raise Exception("n and p should be non-negative")
        return num1**num2


myCalculator = Calculator()
T = int(input())
for i in range(T):
    n, p = map(int, input().split())
    try:
        ans = myCalculator.power(n, p)
        print(ans)
    except Exception as e:
        print(e)
