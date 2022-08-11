# [1,2,4,54,523,52,5,52,525,0,75,8,9,97,0,70,5,7,346,3,5]
# 0 -> 525, 75
#
# first neighbors

def find_first_neighbors(numbers:list[int], target:int) -> list[int]:

    # numbers is empty or None
    # check datatypes
    # decimals/floats
    # correct number of parameters
    # return type
    # test sample with multiple matches

    for i, number in enumerate(numbers):
        if number == target:
            first_match_at = i
            break
    else:
        raise ValueError(f'{target} is not in the list')

    if first_match_at == 0:
        right_neighbor = numbers[first_match_at + 1]
        neighbors = [right_neighbor]
    else:
        left_neighbor = numbers[first_match_at - 1]
        right_neighbor = numbers[first_match_at + 1]
        neighbors = [left_neighbor, right_neighbor]
    return neighbors


