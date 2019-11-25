import random
from typing import *


class Generator:
    """
    Problem instance generator.
    Useful for P||C max.
    Algorithm creates set of tasks which can be optimally scheduled to take
    exactly optimal_time.
    """
    def __init__(self, processors: int):

        self.processors: int = processors
        self.optimal_time: int = random.randint(100, 10000)
        self.tasks = list()
        self.OUTPUT_FILE_NAME = "inputs.txt"
        self.generate()
        self.safe_to_file()

    def generate(self):
        """
        Generation consist of n-timing dividing optimal_time to set of tasks,
        then we know, that it could be optimally arranged to take optimal_time.
        Entire operation is repeated for every processor
        :return:
        """
        print("Generating inputs file")
        print("Optimal time is: {}".format(self.optimal_time))
        print("Processors count is: {}".format(self.processors))
        for processor in range(self.processors):
            free_time = self.optimal_time
            while free_time > 10:
                task_time = random.randint(1, free_time)
                free_time -= task_time
                self.tasks.append(task_time)

            if free_time > 0:
                self.tasks.append(free_time)
        print("Generated {} tasks".format(len(self.tasks)))

    def safe_to_file(self):
        """
        Saving to file is in random order so, prevents decreasing presorting
        of tasks, caused by pore random algorithm, which will
        consecutively chose values exactly in between average, or lack of entropy in system
        :return:
        """
        with open(self.OUTPUT_FILE_NAME, "w") as file:
            file.write("{}\n{}\n".format(
                self.processors,
                len(self.tasks)
            ))
            while len(self.tasks) > 0:
                position = random.randint(0, len(self.tasks) - 1)
                file.write(
                    str(self.tasks[position]) + "\n")
                self.tasks.pop(position)


if __name__ == "__main__":
    Generator(10)
