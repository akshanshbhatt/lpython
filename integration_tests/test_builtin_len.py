from ltypes import i32, f64

def test_len():
    s: str
    s = "abcd"
    assert len(s) == 4
    s = ''
    assert len(s) == 0
    assert len("abcd") == 4
    assert len("") == 0

    l: list[i32]
    l = [1, 2, 3, 4]
    assert len(l) == 4
    l2: list[f64]
    l2 = [1.2, 3.4, 5.6, 7.8, 9.0]
    assert len(l2) == 5

    l3: list[i32] = []
    assert len(l3) == 0
    i: i32
    for i in range(50):
        l3.append(i)
    assert len(l3) == 50

    list_len: i32 = len([1.0, 2.0])
    assert list_len == 2

test_len()
