import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../')))

from constants import const

def set_pi() -> const:
    num = const("pi", 3.142)
    print(num.release())
    return num

def test_reassignment(pi: const) -> None:
    try:
        pi.pi = 3.1425
    except RuntimeError as e:
        assert str(e) == "Cannot reassign const attribute: pi"

if __name__ == "__main__":
    pi = set_pi()
    assert pi.release() == {'pi': 3.142}
    test_reassignment(pi)
