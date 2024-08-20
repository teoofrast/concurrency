import cProfile
import pstats
import io
import tracemalloc
import asyncio

from create_files import create_files_concurrently


def time_profile_create_files():
    """
    Профилирование по времени запись данных в текстовый файл
    """
    pr = cProfile.Profile()
    pr.enable()
    asyncio.run(create_files_concurrently())
    pr.disable()
    s = io.StringIO()
    sortby = 'cumulative'
    ps = pstats.Stats(pr, stream=s).sort_stats(sortby)
    ps.print_stats()
    with open('results/time_profile_create_files.txt', 'w') as file:
        file.write(s.getvalue())


def memory_profile_create_files():
    """
    Профилирование по памяти запись данных в текстовый файл
    """
    tracemalloc.start()
    asyncio.run(create_files_concurrently())
    snapshot = tracemalloc.take_snapshot()
    stats = snapshot.statistics('lineno')
    with open('results/memory_profile_create_files.txt', 'w') as f:
        for stat in sorted(stats, key=lambda x: x.size, reverse=True):
            f.write(f"{stat}\n")


if __name__ == '__main__':
    time_profile_create_files()
    memory_profile_create_files()
