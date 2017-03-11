from invest import Invest


def test_invest(problems):
    for problem in problems:
        a = Invest(problem)
        a.Solve()
        a.status_list[0]
        a.status_list[1]
