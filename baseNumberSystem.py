import pprint


def base_number_system(start: int, end: int, base: int) -> list[str]:
    """Returns a list of exponential numbers"""

    if base < 2 or start < 0:
        return []
    list_of_exponential_numbers = [
        base**exponent for exponent in range(start, end + 1)
    ]
    list_of_exponential_numbers.insert(0, f"base {base}:")
    return list_of_exponential_numbers


print()


def main() -> None:
    """Main function"""

    pp = pprint.PrettyPrinter(underscore_numbers=True, width=200)

    pp.pprint(base_number_system(start=0, end=12, base=2))
    pp.pprint(base_number_system(start=0, end=12, base=3))
    pp.pprint(base_number_system(start=0, end=12, base=4))
    pp.pprint(base_number_system(start=0, end=12, base=5))
    pp.pprint(base_number_system(start=0, end=12, base=6))


if __name__ == "__main__":
    main()
