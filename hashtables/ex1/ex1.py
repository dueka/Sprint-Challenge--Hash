def get_indices_of_item_weights(weights, length, limit):
    cache = {}

    """
    YOUR CODE HERE
    """
    for i in range(0, length):
        current_weight = weights[i]
        # (cache, current_weight, i)
        diff = limit - current_weight
        result = diff
        if result in cache:
            if length == 2:
                return (1, 0)
            return (i, result)
        return None


def get_check(check):
    if check is not None:
        print(str(check[0] + "_" + check[1]))
    else:
        print("None")


# >> > x = {1: 2}
# >> > print(x)
# {1: 2}

# >> > d = {3: 4, 5: 6, 7: 8}
# >> > x.update(d)
# >> > print(x)
# {1: 2, 3: 4, 5: 6, 7: 8}
