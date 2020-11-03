def baseNumberSystem(start, end, base):
    list_of_exponential_numbers = [
        f"{base ** exponent:,}" for exponent in range(start, end + 1)
        ]
    list_of_exponential_numbers.insert(0, f"base {base}:")
    return list_of_exponential_numbers
    
print()

function_arguments = {
    "first_sequence": {"start": 0, "end": 12, "base": 2},
    "second_sequence": {"start": 0, "end": 12, "base": 3},
    "third_sequence": {"start": 0, "end": 12, "base": 4},
    "fourth_sequence": {"start": 0, "end": 12, "base": 5},
}

for key in function_arguments.keys():
    print(baseNumberSystem(**function_arguments[key]))