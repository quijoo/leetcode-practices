import time
# 装饰器是一个函数
def display_time(func):
    def wrapper(*args):
        t1 = time.time()
        res = func(*args)
        t2 = time.time()
        print("Total Time:{:.4}".format(t2 - t1))
        return res
    return wrapper

def is_prinme(num):
    if num < 2:
        return False
    elif num == 2:
        return True
    else:
        for i in range(2, num):
            if num % i == 0:
                return False
        return True

@display_time
def count_prime_nums(maxnum):
    count = 0
    for i in range(2, maxnum):
        if is_prinme(i):
            count += 1
    return count


if __name__ == "__main__":
    count = count_prime_nums(10000)
    print(count)