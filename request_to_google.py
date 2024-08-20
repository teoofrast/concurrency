import aiohttp
import asyncio


async def async_response_to_google(session: aiohttp.ClientSession, semaphore: asyncio.Semaphore):
    """
    Отправляет запрос на сайт гугла и возвращает статус ответа, сделано при помощи asyncio
    """
    if not isinstance(session, aiohttp.ClientSession) or not isinstance(semaphore, asyncio.Semaphore):
        raise TypeError("Wrong type of session or semaphore")
    async with semaphore:
        resp = await session.get("http://google.com")
        return resp.status


async def fetch_multiple_responses_to_google(limit: int, request_count: int):
    """
    Составляет задачи для отправки запроса на сайт гугла, сделано при помощи asyncio
    """
    if not isinstance(limit, int) or not isinstance(request_count, int):
        raise TypeError("Wrong type of limit or request_count")
    elif limit <= 0:
        raise ValueError("Limit must be greater than zero")
    elif request_count <= 0:
        raise ValueError("Request count must be greater than zero")
    tasks = []
    semaphore = asyncio.Semaphore(limit)
    async with aiohttp.ClientSession() as session:
        for _ in range(request_count):
            task = asyncio.create_task(async_response_to_google(session, semaphore))
            tasks.append(task)
            if len(tasks) == 0:
                continue
            elif len(tasks) % limit == 0:
                await asyncio.sleep(1)
        await asyncio.gather(*tasks)
    return {"status": "ok"}


if __name__ == '__main__':
    asyncio.run(fetch_multiple_responses_to_google(10, 50))
