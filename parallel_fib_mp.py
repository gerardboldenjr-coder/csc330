import multiprocessing
import time

def fib(n):
    if n <= 1:
        return n
    return fib(n - 1) + fib(n - 2)

def worker(n):
    answer = fib(n)
    print("fib(" + str(n) + ") =", answer)

def main():
    nums = [35, 36, 37, 38, 39]
    kids = []

    start = time.time()

    for n in nums:
        p = multiprocessing.Process(target=worker, args=(n,))
        kids.append(p)
        p.start()

    for p in kids:
        p.join()

    end = time.time()
    total = end - start

    print("\nTotal time:", total, "seconds")

if __name__ == "__main__":
    main()
