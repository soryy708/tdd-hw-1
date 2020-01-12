
def bblSort(tpl):
    """
        Given unsorted tuple `tpl`, return a sorted copy of `tpl`, using bubble sort (O(n^2) complexity)
    """
    lst = list(tpl)
    for i in range(len(lst) - 1, 0, -1):
        for j in range(i):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]
    return tuple(lst)
