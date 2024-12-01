class Solution:
    def fib(self, n: int) -> int:
        fibonacci_series = [0, 1]
        if (n == 0):
            return 0
        if (n == 1):
            return 1
        else:
            for i in range(n-1):
                fibonacci_series.append((fibonacci_series[-1] + fibonacci_series[-2]))
        return fibonacci_series[-1]