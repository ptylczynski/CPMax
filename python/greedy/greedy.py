from typing import *

from utilities.ConfigReader import ConfigReader, AvailableAlgorithms, ConfigFields
from utilities.read_input import Inputs
from utilities.task import TaskList


class Greedy:
    """
    Greedy algorithm to slove P||C max problem.
    Solution is to find first "empty" processor and assign
    to it next task, from task list.
    Empty processor means processor which as first completes
    all his tasks
    :return:
    """
    def __init__(self):
        self.config: ConfigReader = ConfigReader()
        self.is_sorted: bool = self.config.get_bool(AvailableAlgorithms.GREEDY, ConfigFields.IS_TASK_LIST_SORTED)
        self.inputs: Inputs = Inputs(sort=self.is_sorted)
        self.processors: List[TaskList] = [TaskList() for x in range(self.inputs.processors)]

    def run(self) -> List[TaskList]:
        for task in self.inputs.task_list:
            self.processors[self.find_empty_core()].add(task)
        print()
        print("Cmax for greedy algorithm is: {}".format(self.processors[self.find_max()].total_time()))
        return self.processors

    def find_empty_core(self) -> int:
        minimal = self.processors[0].total_time()
        pos = 0
        for i in range(len(self.processors)):
            if self.processors[i].total_time() < minimal:
                minimal = self.processors[i].total_time()
                pos = i
        return pos

    def find_max(self) -> int:
        maximal = 0
        pos = 0
        for i in range(len(self.processors)):
            if self.processors[i].total_time() > maximal:
                pos = i
                maximal = self.processors[i].total_time()
        return pos


if __name__ == "__main__":
    Greedy().run()
