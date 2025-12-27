import pytest


def add(n,v):
    return int(n+v)

def test_add():
    assert add(3,2) == 5
<<<<<<< Updated upstream:mod3_pract/my_pytest.py

=======
    assert add(14,12) == 26

def test_negative():
    with pytest.raises(TypeError):
        add('12',2)
# def test_val():
#     with pytest.raises(ValueError):
#         add(,2)
>>>>>>> Stashed changes:mod3_pract/pytest_my.py
