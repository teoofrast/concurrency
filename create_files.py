import asyncio
import aiofiles
from pathlib import Path

base_dir = Path(__file__).parent.absolute()

async def create_file(index: int) -> int:
    """
    Корутина для создания текстового файла и записи в него индекса
    """
    if not isinstance(index, int):
        raise TypeError("Index must be an integer.")
    elif index <= 0:
        raise ValueError("Index must be positive.")
    async with aiofiles.open(f"{base_dir}/files/file_{index}.txt", "w", encoding="utf-8") as f:
        await f.write(str(index))
    return index


async def create_files_concurrently():
    """
    Корутина для создания задач
    """
    tasks = [create_file(i) for i in range(1, 11)]
    await asyncio.gather(*tasks)
    return {"status": "ok"}

if __name__ == '__main__':
    asyncio.run(create_files_concurrently())
