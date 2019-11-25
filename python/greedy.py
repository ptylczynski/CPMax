import time

from read_input import Inputs
from generator import Generator


def main():
    """
    Greedy algorithm to slove P||C max problem.
    Solution is to find first "empty" processor and assign
    to it next task, from task list.
    Empty processor means processor which as first completes
    all his tasks
    :return:
    """
    Generator(10)
    inputs = Inputs(sort=True)
    processors = [0 for x in range(inputs.processors)]
    for task in inputs.tasks:
        processors[find_empty_core(processors)] += task
    print()
    print("Cmax is: {}".format(processors[find_max(processors)]))


def find_empty_core(processors: list) -> int:
    minimal = processors[0]
    pos = 0
    for i in range(len(processors)):
        if processors[i] < minimal:
            minimal = processors[i]
            pos = i
    return pos


def find_max(processors: list):
    maximal = 0
    pos = 0
    for i in range(len(processors)):
        if processors[i] > maximal:
            pos = i
            maximal = processors[i]
    return pos


if __name__ == "__main__":
    main()
