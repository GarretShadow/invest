from invest import Invest


def test_invest(projects):
    for project in projects:
        Invest(project)
