from enum import Enum
from typing import *

from helper.task import Task


class InsertMethod(Enum):
    FIRST_FREE = 1,
    SELECTED = 2


class Core:
    def __init__(self, core_number: int):
        self.exec_time = 0
        self.backstack = []
        self.number = core_number

    def __str__(self):
        return "Core number: {}, tasks: {}, total exec time: {}".format(
            self.number,
            self.backstack,
            self.exec_time
        )

    def __repr__(self):
        return self.__str__()

    def add(self, task: Task):
        self.backstack.append(task)
        self.exec_time += task.get_time()

    def get_exec_time(self) -> int:
        return self.exec_time

    def get_core_number(self) -> int:
        return self.number


class Processor:
    def __init__(self, cores_quantity: int, insert_method: InsertMethod):
        self.cores_quantity = cores_quantity
        self.cores = [Core(i) for i in range(self.cores_quantity)]
        self.insert_method = insert_method

    def add_task(self, task: Task):
        if self.insert_method == InsertMethod.FIRST_FREE:
            core_to_add_to = self.find_first_free()
            self.cores[core_to_add_to].add(task)
        else:
            raise Exception("Specify core number")

    def find_first_free(self):
        first_free = 0
        for core in self.cores:
            if core.get_exec_time() < self.cores[first_free].get_exec_time():
                first_free = core.get_core_number()
        return first_free

    def dump_cores(self):
        return self.cores
