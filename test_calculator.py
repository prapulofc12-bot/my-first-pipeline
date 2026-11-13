from calculator import add

def test_add():
    assert add(2, 3) == 5
    print("All tests passed inside container!")

if __name__ == "__main__":
    test_add()
