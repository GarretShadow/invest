import json
import itertools


class Invest:
    def __init__(self, data):
        self.data = data
        self.status_list = []
        self.status_list_next_step = []


    def init(self):
        prj = [-1] * len(self.data['projects'])
        vector = self.generate_projects_times(prj, 0)
        for mas in vector:
            self.convert(prj, mas)
        self.status_list = self.status_list_next_step
        self.status_list_next_step.clear()


    def solve(self):
        self.init()
        for time in self.data['period']:
            self.next_step(time + 1)


    def check_status(self, status: Status):
        result = True
        i = 0
        for res in status.invest:
            # возможны изменения в способе хранения
            if res > self.data['resources'][i]:
                result = False
                break
        return result


    def convert(self, base: list, change: list):
        mas = []
        end_prj = True
        i, j = 0, 0
        for pr in base:
            mas.append(pr)
            if pr != -1:
                # проект выполняется за период планирования
                if self.data['period'] - change[j] > self.data['projects'][i]['length']:
                    mas[i] = change[j]
                    j = j + 1
                else:
                    #проект вышел за горизонт планирования
                    end_prj = False
                    break
            i = i + 1
        if end_prj == True:
            status = Status(mas, self.data)
            if self.check_status(status) == True:
                self.add_to_status_list(status)


    def add_to_status_list(self, status: Status):
        if self.status_list_next_step[0].NPV < status.NPV:
            self.status_list_next_step[0:0] = status


    def next_step(self, time: int):
        for status in self.status_list:
            self.status_list_next_step.append(status)
            vector = self.generate_projects_times(status.projects, time)
            for mas in vector:
                self.convert(status.projects, mas)
        self.status_list = self.status_list_next_step
        self.status_list_next_step.clear()


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








class Status:
    def __init__(self, prj: list, data):
        self.projects = prj
        self.invest = [0] * len(data['period'])
        self.NPV, self.E, self.D = 0, 0, 0
        i = 0
        for pr in self.projects:
            if pr != -1:
                period = pr + data["projects"][i]["lenght"]
                count = pr
                for inv in invest:
                    # считать INV с учетом интервальности
                    inv = data['projects'][i][count - pr]
                    if count < period:
                        break
                #считать NPV с учетом интервальности
                NPV = NPV + data['projects'][i][pr]
                #посчитать МО и ДИСП
                i = i + 1