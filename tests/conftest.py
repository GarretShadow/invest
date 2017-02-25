import glob
import json
import os

import pytest


@pytest.fixture
def project_dir():
    return os.path.dirname(os.path.dirname(os.path.realpath(__file__)))


@pytest.fixture
def problems_dir(project_dir):
    return os.path.join(project_dir, 'data')


@pytest.fixture
def problems(problems_dir):
    problems_list = []
    for file_name in glob.glob(os.path.join(problems_dir, 'data/*.json')):
        with open(file_name) as f:
            problems_list.append(json.load(f))
    return problems_list
