from pynenv.environment import get_environment_variable

def test_get_environment_variable():
    env_var = get_environment_variable('HOME')
    assert env_var == '/home/nsheridan'