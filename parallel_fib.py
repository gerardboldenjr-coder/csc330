import os
import time

def fib(n):
    if n <= 1:
        return n
    return fib(n - 1) + fib(n - 2)

def main():
    nums = [35, 36, 37, 38, 39]
    kids = []

    start = time.time()

    for n in nums:
        pid = os.fork()

        if pid == 0:
            answer = fib(n)
            print("fib(" + str(n) + ") =", answer)
            os._exit(0)
        else:
            kids.append(pid)

    for i in kids:
        os.wait()

    end = time.time()
    total = end - start

    print("\nTotal time:", total, "seconds")

if __name__ == "__main__":
    main()
