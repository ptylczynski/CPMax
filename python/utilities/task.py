from typing import *


class Task:
    def __init__(self, time):
        self.time: int = time

    def get_time(self) -> int:
        return self.time

    def __str__(self):
        return str(self.time)

    def __repr__(self):
        return str(self.time)

    def __lt__(self, other):
        if self.time < other.time:
            return True
        else:
            return False


class TaskList:
    def __init__(self):
        self.current_index: int = 0
        self.task_list: List[Task] = list()

    def add(self, task: Task, pos: int = -1):
        if pos == -1:
            pos = len(self.task_list)
        self.task_list.insert(pos, task)

    def total_time(self) -> int:
        total = 0
        for t in self.task_list:
            total += t.get_time()
        return total

    def remove(self, task: Task):
        self.task_list.remove(task)

    def sort(self,):
            self.task_list.sort()

    def get(self, pos: int) -> Task:
        return self.task_list[pos]

    def __len__(self):
        return len(self.task_list)

    def __iter__(self):
        self.current_index = 0
        return self

    def __next__(self):
        if self.current_index >= len(self.task_list):
            raise StopIteration
        else:
            result = self.task_list[self.current_index]
            self.current_index += 1
            return result

    def __repr__(self):
        return str(self.task_list)

    def __str__(self):
        return str(self.task_list)
