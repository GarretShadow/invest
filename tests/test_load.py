import os
from invest import Invest


def test_load_json(problems_dir):
    Invest.from_json(os.path.join(problems_dir, 'problem01.json'))
