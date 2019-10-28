import time

from read_input import Inputs


def main():
    inputs = Inputs()
    processors = [0 for x in range(inputs.processors)]
    time_start = time.time() * 1000
    for task in inputs.tasks:
        processors[find_empty_core(processors)] += task
    time_end = time.time() * 1000
    print("Time: " + str(time_end - time_start) + "ms")


def find_empty_core(processors: list) -> int:
    minimal = processors[0]
    pos = 0
    for i in range(len(processors)):
        if processors[i] < minimal:
            minimal = processors[i]
            pos = i
    return pos


if __name__ == "__main__":
    main()
