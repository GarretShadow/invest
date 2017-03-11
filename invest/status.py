class Status:
    projects, invest = [], []
    NPV, E, D = 0, 0, 0

    def __init__(self, prj: list, data):
        self.projects = prj
        invest = [0] * len(data['period'])
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