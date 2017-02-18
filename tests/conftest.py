import glob
import json
import os

import pytest

PROJECT_DIR = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))


@pytest.fixture
def projects():
    projects_list = []
    for file_name in glob.glob(os.path.join(PROJECT_DIR, 'data/*.json')):
        with open(file_name) as f:
            project = json.load(f)
            projects_list.append(project)
    return projects_list
