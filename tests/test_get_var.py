import os
import pytest
from dotenv import load_dotenv
from pynenv.environment import get_environment_variable


def test_get_environment_variable():
    test_dir = os.path.dirname(__file__)
    load_dotenv(dotenv_path=f'{test_dir}/.env.mock')
    want = "mock home"
    got = get_environment_variable('MOCK_HOME')
    assert want == got


def test_empty_environment_variable():
    test_dir = os.path.dirname(__file__)
    env_var = 'MOCK_EMPTY'
    load_dotenv(dotenv_path=f'{test_dir}/.env.mock')
    with pytest.raises(AssertionError, match=f"environment variable {env_var} empty"):
        got = get_environment_variable(env_var)


def test_missing_environment_variable():
    test_dir = os.path.dirname(__file__)
    env_var = 'MOCK_MISSING'
    load_dotenv(dotenv_path=f'{test_dir}/.env.mock')
    with pytest.raises(AssertionError, match=f"environment variable {env_var} not set"):
        got = get_environment_variable(env_var)
