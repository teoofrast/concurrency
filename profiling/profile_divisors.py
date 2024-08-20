import cProfile
import pstats
import io
import tracemalloc

from divisors import divisor


def time_profile_divisors(n):
    """
    Профилирование по времени запись данных в текстовый файл
    """
    pr = cProfile.Profile()
    pr.enable()
    divisor(n)
    pr.disable()
    s = io.StringIO()
    sortby = 'cumulative'
    ps = pstats.Stats(pr, stream=s).sort_stats(sortby)
    ps.print_stats()
    with open('results/time_profile_divisors.txt', 'w') as file:
        file.write(s.getvalue())


def memory_profile_divisors(n):
    """
    Профилирование по памяти запись данных в текстовый файл
    """
    tracemalloc.start()
    divisor(n)
    snapshot = tracemalloc.take_snapshot()
    stats = snapshot.statistics('lineno')
    with open('results/memory_profile_divisors.txt', 'w') as f:
        for stat in sorted(stats, key=lambda x: x.size, reverse=True):
            f.write(f"{stat}\n")


if __name__ == '__main__':
    number = 10_000_000
    time_profile_divisors(number)
    memory_profile_divisors(number)
