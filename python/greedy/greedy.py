from utilities.ConfigReader import ConfigReader, AvailableAlgorithms, ConfigFields
from utilities.read_input import Inputs


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
        self.config = ConfigReader()
        self.is_sorted = self.config.get_bool(AvailableAlgorithms.GREEDY, ConfigFields.IS_TASK_LIST_SORTED)
        self.inputs = Inputs(sort=self.is_sorted)
        self.processors = [0 for x in range(self.inputs.processors)]

    def run(self):
        for task in self.inputs.tasks:
            self.processors[self.find_empty_core()] += task
        print()
        print("Cmax is: {}".format(self.processors[self.find_max()]))

    def find_empty_core(self) -> int:
        minimal = self.processors[0]
        pos = 0
        for i in range(len(self.processors)):
            if self.processors[i] < minimal:
                minimal = self.processors[i]
                pos = i
        return pos

    def find_max(self) -> int:
        maximal = 0
        pos = 0
        for i in range(len(self.processors)):
            if self.processors[i] > maximal:
                pos = i
                maximal = self.processors[i]
        return pos


if __name__ == "__main__":
    Greedy().run()
