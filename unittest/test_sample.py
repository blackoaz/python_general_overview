def test_sum():
    assert sum([1, 2, 3]) == 6, "Should be 6"

def test_length():
    assert len([0, 1, 2]) > 0, "Should be 3"

def test_reversed():
    assert list(reversed([1, 2, 3])) == [3, 2, 1]

def test_membership():
    assert 3 in [1, 2, 3]

def test_isinstance():
    assert isinstance([1, 2, 3], list)

def test_all():
    assert all([True, True, True])

def test_any():
    assert any([False, True, False])

def test_always_fail():
    assert pow(10, 2) == 42