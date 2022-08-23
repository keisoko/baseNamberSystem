"""
Outputs a list containing the a series of exponential numbers 
based on the  exponent range e.g. 2⁰ = 1, 2¹ = 2, 2² = 4, etc.
"""

import pprint
from dataclasses import dataclass


@dataclass(frozen=True)
class ConstantNamespace:
    """Class to hold constant names"""

    START = 0


constant = ConstantNamespace()


class WrongBaseAndLowStartError(Exception):
    """Custom Error Class"""

    def __str__(self):
        return "Base must start with 2 and constant.START must be 0 and above."


def base_number_system(end: int, base: int) -> list[str]:
    """Returns a list of exponential numbers"""

    if base < 2 or constant.START < 0:
        raise WrongBaseAndLowStartError()
    list_of_exponential_numbers = [
        base**exponent for exponent in range(constant.START, end + 1)
    ]
    list_of_exponential_numbers.insert(0, f"base {base}:")
    return list_of_exponential_numbers


print()


def execute_main() -> None:
    """Main function"""

    pp = pprint.PrettyPrinter(underscore_numbers=True, width=200)

    pp.pprint(base_number_system(end=12, base=2))
    pp.pprint(base_number_system(end=12, base=3))
    pp.pprint(base_number_system(end=12, base=4))
    pp.pprint(base_number_system(end=12, base=5))
    pp.pprint(base_number_system(end=12, base=6))


if __name__ == "__main__":
    execute_main()
