def add_two_numbers(a: float, b: float) -> float:
    """
    Add two numbers and return the result.

    :param a: The first number
    :param b: The second number
    :return: The sum of a and b
    """
    return a + b

# Example usage
if __name__ == "__main__":
    num1 = 5
    num2 = 10
    result = add_two_numbers(num1, num2)
    print(f"The sum of {num1} and {num2} is {result}.")
