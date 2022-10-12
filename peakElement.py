def findPeakElement(n: int, arr: list) -> int:
    """Find the index of highest element in an array

    Args:
        n (int): length of array
        arr (list): list of random number

    Returns:
        int: index of peak element
    """
    
    return arr.index(max(arr))