import multiprocessing as mp


def find_divisors(number: int, start: int, end: int) -> list:
    """
    Находит все делители заданного числа в указанном диапазоне
    """
    if not isinstance(number, int):
        TypeError('Number must be an integer.')
    if 1_000_000 <= number <= 20_000_000:
        divisors = []
        for i in range(start, end + 1):
            if number % i == 0:
                divisors.append(i)
                if i != number // i:
                    divisors.append(number // i)
        divisors.sort()
        return divisors
    else:
        raise ValueError("Число должно быть в промежутке от 1 000 000 до 20 000 000")


def divisor(n: int, num_of_processes: int=6):
    """
    Находит все делители заданного числа с помощью параллельной обработки.
    """
    if not isinstance(n, int):
        TypeError('Number must be an integer.')
    square = int(n ** 0.5) + 1
    chunk = square // num_of_processes
    pool = mp.Pool(num_of_processes)
    tasks = []
    for i in range(1, square, chunk):
        start = i
        end = min(i + chunk, square)
        tasks.append((n, start, end))
    results = pool.starmap(find_divisors, tasks)
    all_results = [item for sublist in results for item in sublist]
    return sorted(set(all_results))


if __name__ == '__main__':
    print(divisor(int(input("Введите число для поиска делителей: "))))
