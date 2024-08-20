import pytest
import subprocess
import aiohttp
import asyncio

from pathlib import Path

@pytest.fixture(scope='session', autouse=True)
def delete_files():
    """
    Фикстура удаляет файлы в папке files после тестов
    """
    yield
    base_dir = Path(__file__).parent.parent.absolute()
    path_files = f'{base_dir}/files/'
    path = Path(path_files)
    subprocess.run(['sudo', 'rm', '-rf', path])
    subprocess.run(['mkdir', path])
