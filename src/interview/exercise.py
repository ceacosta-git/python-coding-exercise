# [1,2,4,54,523,52,5,52,525,0,75,8,9,97,0,70,5,7,346,3,5]
# 0 -> 525, 75
#
# first neighbors

def find_first_neighbors(numbers: list[int], target: int) -> list[int]:
    # check datatypes
    # decimals/floats
    # correct number of parameters
    # return type
    # test sample with multiple matches
    if numbers is None:
        raise ValueError(f'{target} is not in the list')

    for i, number in enumerate(numbers):
        if number == target:
            first_match_at = i
            break
    else:
        raise ValueError(f'{target} is not in the list')

    target_is_first_element = first_match_at == 0
    target_is_last_element = first_match_at == (len(numbers) - 1)

    if target_is_first_element and target_is_last_element:
        neighbors = []
    elif target_is_first_element:
        right_neighbor = numbers[first_match_at + 1]
        neighbors = [right_neighbor]
    elif target_is_last_element:
        left_neighbor = numbers[first_match_at - 1]
        neighbors = [left_neighbor]
    else:
        left_neighbor = numbers[first_match_at - 1]
        right_neighbor = numbers[first_match_at + 1]
        neighbors = [left_neighbor, right_neighbor]
    return neighbors
