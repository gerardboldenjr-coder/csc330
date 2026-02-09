import time

def fib(n):
    if n <= 1:
        return n
    return fib(n - 1) + fib(n - 2)

def main():
    nums = [35, 36, 37, 38, 39]

    start = time.time()

    for n in nums:
        answer = fib(n)
        print("fib(" + str(n) + ") =", answer)

    end = time.time()
    total = end - start

    print("\nTotal time:", total, "seconds")

if __name__ == "__main__":
    main()
