import pytest
from src.Database import Database

DEFAULT_SIZE = 3

@pytest.fixture()
def default_db():
    # выполняется до запуска теста
    db = Database(size=DEFAULT_SIZE)

    yield db

    # выполняется после запуска теста
    db.__del__()
    db.rm_cache()
    del db
