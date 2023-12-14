list_of_inputs = [1, 2, 3, 4, 5]


def square_root(x: int) -> float:
    return x * (1 / 2)


def is_even(x: int) -> bool:
    return x %2 == 0


res = list(square_root, filter(is_even, list_of_inputs)))
