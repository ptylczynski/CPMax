import configparser
import os
from enum import Enum


class ConfigFields(Enum):
    IS_TASK_LIST_SORTED = 2
    INIT_TEMP_MODIFIER = 3
    LOWEST_TEMPERATURE = 5
    MAX_SOLUTION_ERROR = 4
    ITERATION_COUNT_MODIFIER = 6
    INSERTION_TO_SWAP_BALANCE = 7
    ANNEALING_COEFFICIENT = 8
    BAD_SOLUTION_ACCEPTANCE_THRESHOLD = 9
    ENERGY_ROOT = 10


class AvailableAlgorithms(Enum):
    GREEDY = 1,
    ANNEALING = 2


class ConfigReader:
    """
    API mainly for tuning metaheuristic. It reflects same properties for both greedy and meta.
    Class each time checks if all fields in config file exist, and if not creates it
    """
    def __init__(self):
        self.config_file = os.getcwd() + os.path.sep + "config.ini"
        self.config_parser = configparser.ConfigParser()
        self.is_integral = True

        self.read_config_file()
        self.check_integrity()

    def read_config_file(self):
        try:
            self.config_parser.read(self.config_file)
            print("Config file opened successful")
        except configparser.MissingSectionHeaderError:
            self.config_parser = configparser.ConfigParser()
            print("Missing Section Header, creating new config file")

    def save_config_file(self):
        with open(self.config_file, "w") as file:
            self.config_parser.write(file)
            print("Config file saved")

    def get_int(self, algorithm: AvailableAlgorithms, field: ConfigFields):
        return self.config_parser.getint(
            section=algorithm.name,
            option=field.name)

    def get_bool(self, algorithm: AvailableAlgorithms, field: ConfigFields):
        return self.config_parser.getboolean(
            section=algorithm.name,
            option=field.name)

    def get_float(self, algorithm: AvailableAlgorithms, field: ConfigFields):
        return self.config_parser.getfloat(
            section=algorithm.name,
            option=field.name)

    def check_integrity(self):
        """
        Integrity checking consist of two parts,
        first we check if all sections exist, then we check
        if some fields are not missing. Dividing integrity check prevents
        situations in which we know that entire sections gone, but algorithm naive
        check if maybe some key pairs exist. In this situation we clearly know
        they not.
        :return:
        """
        print("Checking integrity of config file")
        self.check_integrity_of_sections()
        self.check_integrity_of_keys()
        if not self.is_integral:
            print("Config file is not integral")
            self.save_config_file()
        else:
            print("Config file is integral")

    def check_integrity_of_keys(self):
        print("Checking integrity of keys")
        for section in AvailableAlgorithms:
            for key in ConfigFields:
                if key.name not in self.config_parser[section.name]:
                    print("{} in {} missing".format(
                        key.name,
                        section.name
                    ))
                    self.create_key_value(key.name, section.name)
                    self.is_integral = False

    def check_integrity_of_sections(self):
        print("Checking integrity of sections")
        for section in AvailableAlgorithms:
            if section.name not in self.config_parser:
                print("Section {} missing".format(section.name))
                self.create_section(section.name)
                self.is_integral = False

    def create_section(self, section_name: str):
        print("Creating section {}".format(section_name))
        self.config_parser[section_name] = {}
        for key in ConfigFields:
            self.create_key_value(key.name, section_name)

    def create_key_value(self, key_name: str, section_name: str):
        print("Creating {} in {}".format(
            key_name,
            section_name
        ))
        self.config_parser[section_name][key_name] = '0'


if __name__ == "__main__":
    ConfigReader()
