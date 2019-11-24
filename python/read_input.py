class Inputs:
    def __init__(self, sort: bool):
        self.FILE_NAME = "inputs.txt"
        self.processors = 0
        self.tasks = list()
        self.task_count = 0
        self.read_input()

        if sort:
            self.sort()

    def read_input(self):
        with open(self.FILE_NAME, "r") as file:
            self.processors = int(file.readline())
            self.task_count = int(file.readline())
            for line in file:
                # print(line)
                self.tasks.append(int(line))

    def sort(self):
        self.tasks = sorted(self.tasks)
