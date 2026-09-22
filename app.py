def add(a, b):
    return a + b;

if __name__ = "__main__":
    print(add(2, 3))

test_app.py:
    from app imprt add

def test_add():
    assert add(2, 3) == 5

requirements.txt:
    pytest
