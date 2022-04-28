def move(start, by, to, n):
    if n == 0:
        return
    move(start, to, by, n-1)
    print("Move {} from {} to {}".format(n, start, to))
    move(by, start, to, n-1)

if __name__ == "__main__":
    move(0, 1, 2, 4)