import time

def climb_recursive(n):
    if n <= 1:
        return 1
    return climb_recursive(n - 1) + climb_recursive(n - 2)

def climb_iterative(n):
    if n <= 1:
        return 1
    prev2 = 1
    prev1 = 1
    for i in range(2, n + 1):
        current = prev1 + prev2
        prev2 = prev1
        prev1 = current
    return prev1

def measure_time(func, n):
    start = time.perf_counter()
    result = func(n)
    end = time.perf_counter()
    return result, round((end - start) * 1000, 5)

values = [10, 20, 30, 35]

print("n  | Відповідь | Рекурсія (мс)  | Ітерація (мс)")
print("-" * 55)

for n in values:
    result_r, time_r = measure_time(climb_recursive, n)
    result_i, time_i = measure_time(climb_iterative, n)
    print(f"{n:<3}| {result_r:<10}| {time_r:<15}| {time_i}")