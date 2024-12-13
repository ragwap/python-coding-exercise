from coding_exercise.domain.model.cable import Cable


class Splitter:

    def __validate(self, cable: Cable, times: int):
        # Commented default implementation
        # valid = True
        # if not valid:
        #     raise ValueError

        if not isinstance(cable, Cable) or not isinstance(times, int):
            raise ValueError("Invalid input types")
        if times < 1 or times > 64:
            raise ValueError("Number of splits should be in range 1 to 64 inclusive")
        if cable.length < 2 or cable.length > 1024:
            raise ValueError("Cable length should be in range 2 to 1024 inclusive")
        if cable.length // (times + 1) < 1:
            raise ValueError("Cannot split cable into valid lengths")

    def split(self, cable: Cable, times: int) -> list[Cable]:
        self.__validate()

        return []
