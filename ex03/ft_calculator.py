class calculator:
    """
    A class to perform scalar operations on a vector.
    Supports addition, subtraction, multiplication, and division
    with a scalar.
    """

    def __init__(self, vector: list[float]) -> None:
        """
        Initializes the calculator with a vector of floats.

        Args:
            vector (list[float]): The vector to operate on.
        """
        self.vector = vector

    def __add__(self, scalar: float) -> None:
        """
        Adds a scalar to each element of the vector and prints the result.

        Args:
            scalar (float): The scalar to add.
        """
        result = [float(x) + float(scalar) for x in self.vector]
        print(result)

    def __mul__(self, scalar: float) -> None:
        """
        Multiplies each element of the vector by a scalar and prints the
        result.

        Args:
            scalar (float): The scalar to multiply by.
        """
        result = [float(x) * float(scalar) for x in self.vector]
        print(result)

    def __sub__(self, scalar: float) -> None:
        """
        Subtracts a scalar from each element of the vector and prints the
        result.

        Args:
            scalar (float): The scalar to subtract.
        """
        result = [float(x) - float(scalar) for x in self.vector]
        print(result)

    def __truediv__(self, scalar: float) -> None:
        """
        Divides each element of the vector by a scalar and prints the result.

        Args:
            scalar (float): The scalar to divide by.

        Raises:
            ZeroDivisionError: If scalar is 0.
        """
        if scalar == 0:
            raise ZeroDivisionError("Division by zero is not allowed.")
        result = [float(x) / float(scalar) for x in self.vector]
        print(result)
