# PCMax
Metaheuristic algorithm sloving scheduling problem on P equals processors, such a way parallel executions on all processors takes as less time as possible.

Every tasks:
* is uninterruptable
* is undivisable
* is not throwing errors
* is not demanding IO operations
* has after execution delivery time

Projects is written in two languages, Python (fully), C++ (partially)
# Python
Has 4 modules:
1. `ConfigReader` - API for config manipulaiton 
2. `Greedy` - Greedy algorithm to slove PCmax problem
3. `Annealing` - Simulated Annealing metaheuristic
4. `Task` - Model of single `Task`, and `TaskSet`

## `ConfigReader`
Module contains class `ConfigReader`, designed to manipulate config file. It's able to read from config, but as well recreate it entirely, or partilly. During recreation all missing values are set to 0

Module also contains Enums for selection fields to read by `ConfigReader`. They are Algorithm, and Field for particullar algorithm

**Config File Composition**
*TODO fill composition*

## Greedy
Is a greedy algorithm implementation. It sorts list with tasks, such a way longer tasks are first. Then iteratively puts task on processors which time of execution is the shortest.
Cmax will be the largest sum of task time on one of processors

## Annealing
Is a metaheuritsic, depicted in [document](google.com) attached as part of this repository

## Task
First class is `Taks`, which mplements idea of single task to be done in system. In this PCmax version each task is described by it time of execution, so class contains only the time,and some functions to acces it.

In module we can find also `TaksList`, which describe set of tasks. In context of **Greedy** and **Annealing** algorithms it represents all task done on one processor. In context on `InputReader` it depicts all task to be done by system. `TaskList` implements, legth check, lt check, iteration protocol, and reproduce

## Post mortem
All algorithms manipulate on so called *solutions*, which are ordered mappings 'Task' to processors. It is implemented as list of `TaskLists`.

# C++
*TODO Fill docs*
