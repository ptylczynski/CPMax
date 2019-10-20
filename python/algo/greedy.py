from helper.processor import Processor, InsertMethod, Core
from helper.inputs import Inputs
from typing import *


class Greedy:
    def __init__(self):
        self.inputs = Inputs()
        self.processor = Processor(self.inputs.cores_quantity, InsertMethod.FIRST_FREE)
        self.result: List[Core]

    def run(self):
        self.inputs.sort()
        for task in self.inputs:
            self.processor.add_task(task)

        print(self.processor.dump_cores())
