from helper.constants import Constants
from helper.task import Task


class Inputs():
    def __init__(self):
        self.amount = 0
        self.cores_quantity = 0
        self.tasks = []
        self.pos = -1

        self._read_file()

    def __iter__(self):
        return self

    def __next__(self):
        self.pos += 1
        if self.pos >= self.amount:
            raise StopIteration
        else:
            return self.tasks[self.pos]

    def _read_file(self):
        with open(Constants.INPUTS_FILE.value, "r") as file:
            self.cores_quantity = int(file.readline())
            self.amount = int(file.readline())
            for i in range(self.amount):
                self.tasks.append(Task(int(file.readline())))
            print(self.tasks)

    def get_task(self, position: int) -> int:
        if position < self.amount:
            return self.tasks[position]
        else:
            raise Exception("Bad position")

    def get_task_amount(self) -> int:
        return len(self.tasks)

    def sort(self):
        self.tasks = sorted(self.tasks, key=lambda x: x.get_time())
