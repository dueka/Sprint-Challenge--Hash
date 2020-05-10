def has_negatives(a):
    """
    YOUR CODE HERE
    """
    cache = {}
    result = []

    for index, number in enumerate(a):
        if number in cache:
            result.append(abs(number))
        cache[-number] = number

    return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
