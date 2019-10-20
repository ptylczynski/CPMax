from helper.constants import Constants


class Inputs():
    def __init__(self):
        self.amount = 0
        self.times = []

        self._read_file()

    def _read_file(self):
        with open(Constants.INPUTS_FILE.value, "r") as file:
            self.amount = file.readline()
            for i in range(self.amount):
                self.times[i] = file.readline()

    def get_time(self, position: int):
        if position < self.amount:
            return self.times[position]
        else:
            raise Exception("Bad position")

    def sort(self):
        self.times = sorted(self.times)
