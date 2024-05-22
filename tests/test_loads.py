import os
import pytest
from dotenv import load_dotenv
from pynenv.environment import json2dict, yaml2dict


def test_json2dict_load():
    test_dir = os.path.dirname(__file__)
    want = {
        "one": 1,
        "two": 2
    }
    got = json2dict(f'{test_dir}/test_json.json')
    assert want == got

def test_json2dict_type():
    test_dir = os.path.dirname(__file__)
    got = type(json2dict(f'{test_dir}/test_json.json'))
    assert  got== type(dict()) or got == type(list())

def test_yaml2dict_load():
    test_dir = os.path.dirname(__file__)
    want = {
        "one": 1,
        "two": 2
    }
    got = yaml2dict(f'{test_dir}/test_yaml.yaml')
    assert want == got

def test_yaml2dict_type():
    test_dir = os.path.dirname(__file__)
    got = type(yaml2dict(f'{test_dir}/test_yaml.yaml'))
    assert  got== type(dict()) or got == type(list())