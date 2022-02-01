"""An example of function definition."""


def my_max(a: int, b: int) -> int:  # signatrue or contract line
    """Returns the largest argument."""  # Docstring for documentation purposes
    if a >= b:
        return a
    else:
        return b


x: int = 6
y: int = 5 + 2
z: int = my_max(x, y)  # x, y are our arguments and x is an expression
print(z)
