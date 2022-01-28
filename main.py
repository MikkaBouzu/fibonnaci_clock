from datetime import datetime

FIB = [5, 3, 2, 1, 1]


def get_time():
    now = datetime.now()
    print(f"It is currently: {now.hour}:{now.minute}")
    hour = datetime.time(now).hour
    # 12 hour system
    if hour > 12:
        hour = hour-12

    minute = datetime.time(now).minute
    # integer division to get minutes in 5 minutes format
    minute = minute // 5
    return hour, minute


def fibonacci_representation(n):
    # simple implementation of the (modified) Zeckendorf algorithm
    if n == 0:
        return [0]
    fib = [5, 3, 2, 1, 1]
    digits = []
    for f in fib:
        if f <= n:
            digits = digits + [1]
            n = n - f
        else:
            digits += [0]
    return digits


def clock_colors(hours, minutes):
    colors = {"R": [],
               "G": [],
               "B": [],
               "0": []}
    fib = [5, 3, 2, 1, 1]
    for h, m, f in zip(hours, minutes, fib):
        if h == 1 and m == 1:
            colors["B"] += [f]
        elif h == 1:
            colors["R"] += [f]
        elif m == 1:
            colors["G"] += [f]
        else:
            colors["0"] += [f]
    return colors


if __name__ == "__main__":
    hours, minutes = get_time()

    fib_hours = fibonacci_representation(hours)
    fib_minutes = fibonacci_representation(minutes)

    print(fib_hours)
    print(fib_minutes)

    colors = clock_colors(fib_hours, fib_minutes)

    print(colors)

