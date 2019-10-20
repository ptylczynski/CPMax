import hashlib


class Task:
    def __init__(self, time):
        self.time = time

    def get_time(self) -> int:
        return self.time

    def __str__(self):
        return "Task exec time: {}".format(
            self.time
        )

    def __repr__(self):
        return self.__str__()
