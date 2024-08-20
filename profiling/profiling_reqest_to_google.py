import cProfile
import pstats
import io
import tracemalloc
import asyncio

from request_to_google import fetch_multiple_responses_to_google


def time_profile_responses_to_google():
    """
    Профилирование по времени запись данных в текстовый файл
    """
    pr = cProfile.Profile()
    pr.enable()
    asyncio.run(fetch_multiple_responses_to_google(10, 100))
    pr.disable()

    s = io.StringIO()
    sortby = 'cumulative'
    ps = pstats.Stats(pr, stream=s).sort_stats(sortby)
    ps.print_stats()

    with open('results/time_profile_request_to_google.txt', 'w') as file:
        file.write(s.getvalue())


def memory_profile_responses_to_google():
    """
    Профилирование по памяти запись данных в текстовый файл
    """
    tracemalloc.start()
    asyncio.run(fetch_multiple_responses_to_google(10, 100))
    snapshot = tracemalloc.take_snapshot()
    stats = snapshot.statistics('lineno')
    with open('results/memory_profile_request_to_google.txt', 'w') as f:
        for stat in sorted(stats, key=lambda x: x.size, reverse=True):
            f.write(f"{stat}\n")


if __name__ == '__main__':
    time_profile_responses_to_google()
    memory_profile_responses_to_google()
