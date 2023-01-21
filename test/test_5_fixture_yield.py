import pytest
from src.Database import Database

def test_initialization_limit(default_db):
    default_db.add(1)
    default_db.add(2)
    default_db.add(3)
    default_db.add(4)
    assert default_db.size == 3, "Database size exceeds initial"

def test_initialization_down_border():
    with pytest.raises(ValueError):
        db = Database(0)

def test_new_element_add(default_db):
    default_db.add(1)
    default_db.add(2)
    assert default_db.data[0] == 2, "Wrong first element"
