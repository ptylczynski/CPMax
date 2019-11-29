import math
from copy import deepcopy
import random

from greedy.greedy import Greedy
from typing import *

from utilities.ConfigReader import ConfigReader, AvailableAlgorithms, ConfigFields
from utilities.read_input import Inputs
from utilities.task import TaskList


class Annealing:
    def __init__(self):
        self.solution: List[TaskList] = list()
        self.inputs: Inputs = Inputs(sort=False)
        self.config: ConfigReader = ConfigReader()
        self.solution = self.get_greedy_solution()
        self.temperature = 0

        # SETTINGS
        ###
        # 2 in paper
        self.iteration_count_modifier = \
            self.config.get_float(AvailableAlgorithms.ANNEALING, ConfigFields.ITERATION_COUNT_MODIFIER)

        # r1 in paper
        self.insertion_to_swap_balance = \
            self.config.get_float(AvailableAlgorithms.ANNEALING, ConfigFields.INSERTION_TO_SWAP_BALANCE)

        # alpha in paper
        self.annealing_coefficient = \
            self.config.get_float(AvailableAlgorithms.ANNEALING, ConfigFields.ANNEALING_COEFFICIENT)

        # epsilon1 in paper
        self.max_solution_error = \
            self.config.get_float(AvailableAlgorithms.ANNEALING, ConfigFields.MAX_SOLUTION_ERROR)

        # K in paper
        self.init_temp_modifier = \
            self.config.get_float(AvailableAlgorithms.ANNEALING, ConfigFields.INIT_TEMP_MODIFIER)

        # epsilon2 in paper
        self.lowest_temperature = \
            self.config.get_float(AvailableAlgorithms.ANNEALING, ConfigFields.LOWEST_TEMPERATURE)

        # r6 in paper
        self.bad_solution_acceptance_threshold = \
            self.config.get_float(AvailableAlgorithms.ANNEALING, ConfigFields.BAD_SOLUTION_ACCEPTANCE_THRESHOLD)

        self.energy_root = \
            self.config.get_float(AvailableAlgorithms.ANNEALING, ConfigFields.ENERGY_ROOT)

        # L
        self.max_iterations_under_same_temperature = \
            (self.inputs.task_count ** 2) / self.iteration_count_modifier

        # LB in paper
        self.lowest_bound = \
            self.inputs.optimal_time

        # T in paper
        self.initial_temperature = \
            self.init_temp_modifier * (self.solution_score(self.solution) / self.lowest_bound)
        ###

    def run(self) -> List[TaskList]:
        self.temperature = self.initial_temperature
        iterations_under_same_temperature = 0
        while   self.temperature > self.lowest_temperature and \
                self.solution_error(self.solution) > self.max_solution_error:
            print()
            print("-------")
            print("Step Statistics: ")
            print("Temperature: {}".format(self.temperature))
            print("Iterations: {}/{}".format(iterations_under_same_temperature, self.max_iterations_under_same_temperature))
            print("Actual error: {}".format(self.solution_error(self.solution)))
            print("-------")
            neighborhood_choose = random.random()
            new_solution: List[TaskList] = list()
            if neighborhood_choose > self.insertion_to_swap_balance:
                # insert neighborhood
                new_solution = self.create_insert_neighborhood()
            else:
                # swap neighborhood
                new_solution = self.create_swap_neighborhood()

            old_solution_score = self.solution_score(self.solution)
            new_solution_score = self.solution_score(new_solution)
            if new_solution_score < old_solution_score:
                self.solution = deepcopy(new_solution)
            else:
                energy = self.energy(new_solution_score - old_solution_score)
                if energy > self.bad_solution_acceptance_threshold:
                    self.solution = deepcopy(new_solution)
            iterations_under_same_temperature += 1
            if iterations_under_same_temperature > self.max_iterations_under_same_temperature:
                self.temperature *= self.annealing_coefficient
                iterations_under_same_temperature = 0


        print("Cmax for annealing algorithm is: {}".format(self.find_cmax()))
        return self.solution

    def get_greedy_solution(self) -> List[TaskList]:
        return Greedy().run()

    def create_swap_neighborhood(self) -> List[TaskList]:
        ###############
        # FIRST TRY
        # Choosing two different processors
        processor1 = random.randrange(0, self.inputs.processors)
        processor2 = random.randrange(0, self.inputs.processors)

        while processor1 == processor2:
            processor1 = random.randrange(0, self.inputs.processors)
            processor2 = random.randrange(0, self.inputs.processors)

        #
        tasks_on_processor1 = len(self.solution[processor1])
        tasks_on_processor2 = len(self.solution[processor2])
        #################
        # REPETITIONS
        # Checking if both have more than 0 tasks ongoing
        while len(self.solution[processor1]) == 0 or len(self.solution[processor2]) == 0:
            processor1 = random.randrange(0, self.inputs.processors)
            processor2 = random.randrange(0, self.inputs.processors)

            while processor1 == processor1:
                processor1 = random.randrange(0, self.inputs.processors)
                processor2 = random.randrange(0, self.inputs.processors)

            tasks_on_processor1 = len(self.solution[processor1])
            tasks_on_processor2 = len(self.solution[processor2])
        ##################
        # Choosing two tasks, they cant be this same, because they are on
        # two different processors
        task1_index = random.randrange(0, tasks_on_processor1)
        task2_index = random.randrange(0, tasks_on_processor2)

        new_solution = deepcopy(self.solution)

        # swapping them places
        # we need to remove each, because python creates references
        task1 = new_solution[processor1].get(task1_index)
        new_solution[processor1].remove(task1)
        task2 = new_solution[processor2].get(task2_index)
        new_solution[processor2].remove(task2)

        new_solution[processor1].add(task2, task1_index)
        new_solution[processor2].add(task1, task2_index)

        return new_solution

    def create_insert_neighborhood(self) -> List[TaskList]:
        ##################################
        # Choosing processor which have at least 3 tasks
        # Swapping 2 tasks is senseless
        processor = random.randrange(0, self.inputs.processors)
        tasks_on_processor = len(self.solution[processor])

        while tasks_on_processor < 2:
            processor = random.randrange(0, self.inputs.processors)
            tasks_on_processor = len(self.solution[processor])
        #################################
        # Choosing to different indexes,
        # this time we need to check if they are other, cuz
        # are on this same processor
        task_take_index = random.randrange(0, tasks_on_processor)
        task_insert_index = random.randrange(0, tasks_on_processor)

        while task_take_index == task_insert_index:
            task_take_index = random.randrange(0, tasks_on_processor)
            task_insert_index = random.randrange(0, tasks_on_processor)
        #################################

        new_solution = deepcopy(self.solution)

        task1 = new_solution[processor].get(task_take_index)
        task2 = new_solution[processor].get(task_insert_index)
        new_solution[processor].remove(task1)
        new_solution[processor].remove(task2)
        new_solution[processor].add(task1, task_insert_index)
        new_solution[processor].add(task2, task_take_index)

        return new_solution
        
    def solution_score(self, solution: List[TaskList]) -> int:
        score = 0
        for task_list in solution:
            score = max(score, task_list.total_time())
        return score

    def solution_error(self, solution: List[TaskList]) -> float:
        return (self.solution_score(solution) - self.lowest_bound) / self.lowest_bound

    def energy(self, score_difference: float) -> float:
        return math.exp(-score_difference / self.temperature)

    def find_cmax(self):
        cmax = 0
        for task_set in self.solution:
            cmax = max(cmax, task_set.total_time())
        return cmax
