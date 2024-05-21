import os
from dotenv import load_dotenv
from pynenv.environment import get_environment_variable


def test_get_environment_variable():
    test_dir = os.path.dirname(__file__) 
    load_dotenv(dotenv_path=f'{test_dir}/.env.mock')
    want = "mock home"
    got = get_environment_variable('MOCK_HOME')
    assert want == got