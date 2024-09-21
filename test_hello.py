from hello import hello

def test_argument():
    assert hello("David") == "hello, David"
def test_default():
    for name in ["Hermione","Harry","Ron"]
    assert hello(name) == f"hello, {name}"