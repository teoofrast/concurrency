import pytest
import asyncio
import aiohttp
import os

from requests_to_example_com import async_response_to_url, fetch_statuses_with_limit, base_dir


@pytest.mark.asyncio
async def test_async_response_to_url():
    """
    Тест работы корутины async_response_to_url
    """
    file_path = f'{base_dir}/files/statuses.txt'
    semaphore = asyncio.Semaphore(1)
    async with aiohttp.ClientSession() as session:
        result = await async_response_to_url(session, semaphore, "https://example.com")
        with open(file_path, 'r') as f:
            assert f.read() == "200\n"
        assert result == 200
        assert os.path.exists(file_path) == True


@pytest.mark.asyncio
async def test_async_response_to_url_negative():
    """
    Тест работы корутины async_response_to_url с неверным типом данных
    """
    with pytest.raises(TypeError):
        await async_response_to_url(aiohttp.ClientSession(), asyncio.Semaphore(10), 1)


@pytest.mark.asyncio
async def test_fetch_statuses_with_limit():
    """
    Тест работы корутины fetch_statuses_with_limit
    """
    result = await fetch_statuses_with_limit(50, 10, "https://example.com")
    assert result["status"] == "ok"


@pytest.mark.asyncio
async def test_fetch_statuses_with_limit_negative():
    """
    Тест работы корутины fetch_statuses_with_limit с неверным типом данных
    """
    with pytest.raises(TypeError):
        await fetch_statuses_with_limit(50, "hello", "https://example.com")


@pytest.mark.asyncio
async def test_fetch_statuses_with_limit_negative_number():
    """
    Тест работы корутины fetch_statuses_with_limit с отрицательным числом
    """
    with pytest.raises(ValueError):
        await fetch_statuses_with_limit(50, -4, "https://example.com")
