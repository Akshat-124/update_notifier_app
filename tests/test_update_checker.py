from update_checker import is_update_available

def test_basic():
    assert isinstance(is_update_available(), bool)
