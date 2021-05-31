from first_package.lib import try_me

def test_try_me():
    assert try_me() == 'WAZZAP MY DUDES'

def test_type_try_me():
    assert isinstance(try_me(), str)
    