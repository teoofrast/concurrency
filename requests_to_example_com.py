import aiohttp
import asyncio
import aiofiles
from pathlib import Path

base_dir = Path(__file__).parent.absolute()


async def async_response_to_url(session: aiohttp.ClientSession, semaphore: asyncio.Semaphore, url: str) -> int:
    """
    Отправляет запрос на сайт и сосздает текстовый файл с ответом сервера
    """
    if not isinstance(semaphore, asyncio.Semaphore) or not isinstance(url, str) or not isinstance(session,
                                                                                                  aiohttp.ClientSession):
        raise TypeError("Wrong type of data")
    async with semaphore:
        resp = await session.get(url)
        async with aiofiles.open(f'{base_dir}/files/statuses.txt', 'a', encoding='utf-8') as f:
            await f.write(f"{str(resp.status)}\n")
            return resp.status


async def fetch_statuses_with_limit(requests_count: int, limit: int, url: str) -> dict:
    """
    Выполняет несколько асинхронных HTTP-запросов с ограничениями по параллельности и записывает статусы в файл.
    """
    if not isinstance(requests_count, int) or not isinstance(limit, int) or not isinstance(url, str):
        raise TypeError("Wrong type of data")
    elif requests_count <= 0 or limit <= 0:
        raise ValueError("Wrong number of requests_count or limit")
    file_path = Path(f'{base_dir}/files/statuses.txt')
    if file_path.exists():
        file_path.unlink()
    semaphore = asyncio.Semaphore(limit)
    async with aiohttp.ClientSession() as session:
        tasks = [async_response_to_url(session, semaphore, url) for _ in range(requests_count)]
        await asyncio.gather(*tasks)
        return {"status": "ok"}


if __name__ == '__main__':
    asyncio.run(fetch_statuses_with_limit(50, 10, 'https://example.com'))
