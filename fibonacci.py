# fib(n) = fib(n-1) + fib(n-2)
# 重叠子问题


# 递归式
# 重复计算 2^n
import time
def time_printer(func):
    def wrapper(*args):
        t1 = time.time()
        res = func(*args)
        t2 = time.time()
        print("Spend Time:{}".format(t2 - t1))
        return res
    return wrapper

@time_printer  
def fib_warpper(nn):  
    def fib(n):
        if n == 1 or n == 2:
            return 1
        return fib(n - 1) + fib(n - 2)
    return fib(nn)
if __name__ == "__main__":
    print(fib_warpper(10))