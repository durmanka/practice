import time

def climb_recursive(n: int) -> int:
    if n <= 2:
        return n
    return climb_recursive(n - 1) + climb_recursive(n - 2)


def climb_iterative(n: int) -> int:
    if n <= 2:
        return n

    a, b = 1, 2
    for _ in range(3, n + 1):
        a, b = b, a + b
    return b


def measure_time(func, n: int):
    start = time.time()
    result = func(n)
    end = time.time()
    return result, end - start


if __name__ == "__main__":
    ns = [10, 20, 30, 35]

    print("n | recursive result | recursive time | iterative result | iterative time")
    print("-" * 80)

    for n in ns:
        rec_res, rec_time = measure_time(climb_recursive, n)
        it_res, it_time = measure_time(climb_iterative, n)

        print(f"{n} | {rec_res} | {rec_time:.6f}s | {it_res} | {it_time:.6f}s")