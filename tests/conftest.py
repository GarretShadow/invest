import glob
import json
import os

import pytest

PROBLEMS_DIR = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))


@pytest.fixture
def problems():
    problems_list = []
    for file_name in glob.glob(os.path.join(PROBLEMS_DIR, 'data/*.json')):
        with open(file_name) as f:
            problems_list.append(json.load(f))
    return problems_list
