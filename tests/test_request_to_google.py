import pytest
import aiohttp
import asyncio

from request_to_google import async_response_to_google, fetch_multiple_responses_to_google


@pytest.mark.asyncio
async def test_async_response_to_google():
    """
    Тест работы корутины async_response_to_google
    """
    semaphore = asyncio.Semaphore(1)
    async with aiohttp.ClientSession() as session:
        result = await async_response_to_google(session, semaphore)
        assert result == 200


@pytest.mark.asyncio
async def test_async_response_to_google_negative():
    """
    Тест работы корутины async_response_to_google с неверным типом данных
    """
    with pytest.raises(TypeError):
        await async_response_to_google(1, 2)


@pytest.mark.asyncio
async def test_fetch_multiple_responses_to_google():
    """
    Тест работы корутины fetch_multiple_response_to_google
    """
    result = await fetch_multiple_responses_to_google(10, 50)
    assert result["status"] == "ok"


@pytest.mark.asyncio
async def test_fetch_multiple_responses_to_google_negative_number():
    """
    Тест работы корутины fetch_multiple_response_to_google с отрицательным числом
    """
    with pytest.raises(ValueError):
        await fetch_multiple_responses_to_google(-1, 10)


@pytest.mark.asyncio
async def test_fetch_multiple_responses_to_google_wrong_type():
    """
    Тест работы корутины fetch_multiple_response_to_google с строкой
    """
    with pytest.raises(TypeError):
        await fetch_multiple_responses_to_google("hello", 10)
