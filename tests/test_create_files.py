import pytest

from create_files import create_file, create_files_concurrently


@pytest.mark.asyncio
async def test_create_file():
    """
    Тест работы функций create_file
    """
    result = await create_file(1)
    assert result == 1
    with open(f'files/file_1.txt', 'r', encoding='utf-8') as f:
        assert f.read() == str(1)


@pytest.mark.asyncio
async def test_create_files_negative():
    """
    Тест работы функций create_file с неправильным типом передаваемого параметра
    """
    with pytest.raises(TypeError):
        await create_file("hello")


@pytest.mark.asyncio
async def test_create_files_negative_number():
    """
    Тест работы функций create_file с отрицательным числом
    """
    with pytest.raises(ValueError):
        await create_file(-1)


@pytest.mark.asyncio
async def test_create_files_concurrently():
    """
    Тест работы функций create_files_concurrently
    """
    result = await create_files_concurrently()
    assert result["status"] == "ok"
