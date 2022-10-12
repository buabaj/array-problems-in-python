def findDuplicates(arr, n):
    """Find duplicates in an array

    Args:
        arr (list): list of random numbers
        n (int): length of array

    Returns:
        list: list of duplicates
    """
    return [x for x in arr if arr.count(x) > 1]
