def linear_search(haystack: list[int], needle: int) -> bool:
    for item in haystack:
        if item == needle:
            return True
    return False


def test_linear_search():
    haystack = [1, 3, 4, 69, 71, 81, 90, 99, 420, 1337, 69420]
    assert linear_search(haystack, 69) is True
    assert linear_search(haystack, 1336) is False
    assert linear_search(haystack, 69420) is True
    assert linear_search(haystack, 69421) is False
    assert linear_search(haystack, 1) is True
    assert linear_search(haystack, 0) is False
