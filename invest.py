import json


class Invest:
    def __init__(self, data):
        self.data = data
        self.status_list = []
        self.status_list_next_step = []
        # prj = [-1] * len(self.data['projects'])
        # self.gray(0, prj, prj)
        # self.status_list = self.status_list_next_step
        # self.status_list_next_step.clear()

    def solve(self):
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

    @classmethod
    def from_json(cls, file):
        data = json.load(file)
        return cls(data)
