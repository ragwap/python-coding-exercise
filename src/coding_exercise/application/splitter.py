from coding_exercise.domain.model.cable import Cable
import math

# Define ranges for times and lengths globally
MIN_TIMES = 1
MAX_TIMES = 64
MIN_LEN = 2
MAX_LEN = 1024

class Splitter:

    def __validate(self, cable: Cable, times: int):

        # Checks if the inputs are of correct formats
        if not isinstance(cable, Cable) or not isinstance(times, int):
            raise ValueError("Invalid input types")
        
        # Checks if times and cable lenghts are within the specified ranges
        if times < MIN_TIMES or times > MAX_TIMES:
            raise ValueError("Number of splits should be in range 1 to 64 inclusive")
        if cable.length < MIN_LEN or cable.length > MAX_LEN:
            raise ValueError("Cable length should be in range 2 to 1024 inclusive")
        
        # Checks if a cable can be split into equal/valid lenghts with the given times
        if cable.length // (times + 1) < 1:
            raise ValueError("Cannot split cable into valid lengths")

    def split(self, cable: Cable, times: int) -> list[Cable]:
        self.__validate(cable, times)

        # Calculate the initial split length and the remainder
        total_splits = times + 1
        split_length = cable.length // total_splits
        remainder = cable.length % total_splits

        counter = 0
        split_arr = [split_length]

        # Handle the remainder
        while remainder > 0:
            # Split the remainder into chunks as close as possible to split_length
            if remainder >= split_length:
                split_arr.append(split_length)
                remainder -= split_length
            else:
                split_arr.append(remainder)
                remainder = 0

            counter += 1

        # If no remainder array: split_length can be taken into account
        if not split_arr:
            gcd = split_length
            res_range = total_splits
        else:
            gcd = math.gcd(*split_arr) # Else: the greatest common divisor should be the length of each cable
            res_range = cable.length // gcd # Calculating the number of cables

        # Find the number of digits in the maximum value to fill zeros
        padding = len(str(res_range))

        result = [Cable(gcd, f"{cable.name}-{i:0{padding}d}") for i in range(res_range)]
        return result