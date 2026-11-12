from calculator import add

def test_add():
    # 2 + 3 must equal 5
    assert add(2, 3) == 5
    print("Test Passed!")

if __name__ == "__main__":
    test_add()
