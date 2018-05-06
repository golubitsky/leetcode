from src import hello_world


def test_say_hi():
    assert hello_world.say_hi() == "Hi!"


def test_add():
    assert hello_world.add(2, 2) == 4
