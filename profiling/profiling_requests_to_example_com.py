import cProfile
import pstats
import io
import tracemalloc
import asyncio

from requests_to_example_com import fetch_statuses_with_limit


def time_profile_fetch_statuses_with_limit():
    """
    Профилирование по времени запись данных в текстовый файл
    """
    pr = cProfile.Profile()
    pr.enable()
    asyncio.run(fetch_statuses_with_limit(50, 10, "https://example.com"))
    pr.disable()
    s = io.StringIO()
    sortby = 'cumulative'
    ps = pstats.Stats(pr, stream=s).sort_stats(sortby)
    ps.print_stats()
    with open('results/time_profile_requests_to_example_com.txt', 'w') as file:
        file.write(s.getvalue())


def memory_profile_fetch_statuses_with_limit():
    """
    Профилирование по памяти запись данных в текстовый файл
    """
    tracemalloc.start()
    asyncio.run(fetch_statuses_with_limit(50, 10, "https://example.com"))
    snapshot = tracemalloc.take_snapshot()
    stats = snapshot.statistics('lineno')
    with open('results/memory_profile_requests_to_example_com.txt', 'w') as f:
        for stat in sorted(stats, key=lambda x: x.size, reverse=True):
            f.write(f"{stat}\n")


if __name__ == '__main__':
    time_profile_fetch_statuses_with_limit()
    memory_profile_fetch_statuses_with_limit()
