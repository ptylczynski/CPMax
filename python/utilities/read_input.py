from utilities.task import Task, TaskList


class Inputs:
    """
    Class reads inputs from file, and saves it to TaskList
    """
    def __init__(self, sort: bool):
        self.FILE_NAME: str = "inputs.txt"
        self.processors: int = 0
        self.task_list: TaskList = TaskList()
        self.task_count: int = 0
        self.total_time: int = 0
        self.optimal_time: int = 0
        self.read_input()
        self.get_optimal_time()

        if sort:
            self.sort()

    def read_input(self):
        with open(self.FILE_NAME, "r") as file:
            self.processors = int(file.readline())
            self.task_count = int(file.readline())
            for line in file:
                # print(line)
                self.task_list.add(
                    Task(int(line))
                )

    def get_optimal_time(self):
        """
        We suppose that best time is average of time and processors, due
        each processor should do same time, or some processors will finish earlier if
        total time is undivisable to integers
        :return:
        """
        for task in self.task_list:
            self.total_time += task.get_time()
        self.optimal_time = self.total_time / self.processors

    def sort(self):
        self.task_list.sort()
