def binary_search(haystack: list[int], needle: int) -> bool:
    low = 0
    high = len(haystack)

    while low < high:
        midpoint = low + (high - low) // 2
        value = haystack[midpoint]

        if value == needle:
            return True
        elif value > needle:
            high = midpoint
        else:
            low = midpoint + 1

    return False


def test_binary_search():
    haystack = [1, 3, 4, 69, 71, 81, 90, 99, 420, 1337, 69420]
    assert binary_search(haystack, 69) is True
    assert binary_search(haystack, 1336) is False
    assert binary_search(haystack, 69420) is True
    assert binary_search(haystack, 69421) is False
    assert binary_search(haystack, 1) is True
    assert binary_search(haystack, 0) is False
