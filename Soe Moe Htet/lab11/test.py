
def powerset(array):
    # Empty set is part of power set
    subsets = [[]]

    print(subsets)
    for element in array:
        # Add every element to existing subsets

        for i in range(len(subsets)):
            subset = subsets[i]
            print(subset)
            subsets.append(subset + [element])
    return subsets


print(powerset([1, 2]))  # [[], [1], [2], [1, 2]]