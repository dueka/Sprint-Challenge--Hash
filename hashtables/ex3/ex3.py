def intersection(arrays):
    """
    YOUR CODE HERE
    """
    cache = {}
    result = []
    # arrays, item = 0, 0
    for array in arrays:
        for i in array:
            if i in cache:
                cache[i] += 1
            else:
                cache[i] = 1

    # while index, number in enumerate(cache):
    # for index, number in enumerate(cache):
    #     if cache[item] + cache[item - 1]:
    #         print(cache[item])
    for index, number in enumerate(cache):
        if cache[number] == len(arrays):
            result.append(number)
    return result


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
