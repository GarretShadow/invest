import json
import itertools


class Invest:
    def __init__(self, data):
        self.data = data
        self.status_list = []
        self.status_list_next_step = []

    def init(self):
        prj = [-1] * len(self.data['projects'])
        self.gray(0, prj, prj)
        self.status_list = self.status_list_next_step
        self.status_list_next_step.clear()

    def solve(self):
        self.init()
        for time in self.data['period']:
            self.next_step(time + 1)

    def gray(self, time: int, change: list, base_list: list, k=0):
        if k == len(change):
            self.convert(base_list, change)
        else:
            change[k] = -1
            self.gray(time, change, base_list, k + 1)
            change[k] = time
            self.r_gray(time, change, base_list, k + 1)

    def r_gray(self, time: int, change: list, base_list: list, k=0):
        if k == len(change):
            self.convert(base_list, change)
        else:
            change[k] = time
            self.gray(time, change, base_list, k + 1)
            change[k] = -1
            self.r_gray(time, change, base_list, k + 1)

    def check_status(self):
        pass

    def convert(self):
        l = []
        end_prj = True

    def init_gray(self):
        pass

    def next_step(self):
        pass

    @staticmethod
    def generate_projects_times(projects_times, time):
        """
        >>> list(Invest.generate_projects_times([-1, 0, 2, -1, -1], 0))
        [[-1, 0, 2, -1, -1], [-1, 0, 2, -1, 0], [-1, 0, 2, 0, -1], [-1, 0, 2, 0, 0], [0, 0, 2, -1, -1], [0, 0, 2, -1, 0], [0, 0, 2, 0, -1], [0, 0, 2, 0, 0]]
        """
        count = projects_times.count(-1)
        for i in itertools.product([-1, time], repeat=count):
            v = list(i)
            result = []
            for j in projects_times:
                if j != -1:
                    result.append(j)
                else:
                    result.append(v.pop(0))
            yield result

    @classmethod
    def from_json(cls, file_name):
        with open(file_name) as f:
            data = json.load(f)
        return cls(data)
