def vector_operation(method):
    """
    Decorator that binds a standalone function to the calculator class,
    allowing the class to use it without instantiation.
    """
    setattr(calculator, method.__name__, staticmethod(method))
    return method


class calculator:
    """
    A vector calculator that performs dot product, addition,
    and subtraction of two same-sized vectors.
    """
    pass


@vector_operation
def dotproduct(V1: list[float], V2: list[float]) -> None:
    """
    Computes and prints the dot product of two vectors.

    Args:
        V1 (list[float]): First vector.
        V2 (list[float]): Second vector.
    """
    result = sum(float(x) * float(y) for x, y in zip(V1, V2))
    print(f"Dot product is: {result}")


@vector_operation
def add_vec(V1: list[float], V2: list[float]) -> None:
    """
    Computes and prints the element-wise addition of two vectors.

    Args:
        V1 (list[float]): First vector.
        V2 (list[float]): Second vector.
    """
    result = [float(x) + float(y) for x, y in zip(V1, V2)]
    print(f"Add Vector is : {result}")


@vector_operation
def sous_vec(V1: list[float], V2: list[float]) -> None:
    """
    Computes and prints the element-wise subtraction of two vectors.

    Args:
        V1 (list[float]): First vector.
        V2 (list[float]): Second vector.
    """
    result = [float(x) - float(y) for x, y in zip(V1, V2)]
    print(f"Sous Vector is: {result}")
