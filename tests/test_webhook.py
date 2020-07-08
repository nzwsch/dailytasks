from dailytasks.webhook import chunks


def test_chunks_divide_by_4():
    lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    assert list(chunks(lst, 4)) == [[1, 2, 3, 4], [5, 6, 7, 8], [9]]


def test_chunks_divide_by_3():
    lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    assert list(chunks(lst, 3)) == [[1, 2, 3], [4, 5, 6], [7, 8, 9]]


def test_chunks_divide_by_2():
    lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    assert list(chunks(lst, 2)) == [[1, 2], [3, 4], [5, 6], [7, 8], [9]]
