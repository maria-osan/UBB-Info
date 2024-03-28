"""
    Pentru un șir cu n numere întregi care conține și duplicate,
    să se determine elementul majoritar (care apare de mai mult de n / 2 ori).
    De ex. 2 este elementul majoritar în șirul [2,8,7,2,2,5,2,3,1,2,2].
"""


# Complextatea temporala: O(n)
# Complextatea spatiala: O(1)
def elem_majoritar(sir):
    elem = None
    nr_aparitii = 0
    for i in sir:
        if nr_aparitii == 0:
            elem = i
            nr_aparitii = 1
        elif i == elem:
            nr_aparitii += 1
        else:
            nr_aparitii -= 1
    return elem


def test():
    assert (elem_majoritar([2, 8, 7, 2, 2, 5, 2, 3, 1, 2, 2]) == 2)
    assert (elem_majoritar([1, 2, 3, 1, 5, 2, 1]) == 1)
    assert (elem_majoritar([1, 2, 5, 1, 5, 3, 5, 7]) == 5)


if __name__ == '__main__':
    test()

# Solutia oferita ce bot (Boyer-Moore Voting Algorithm):
# Complextatea temporala: O(n)
# Complextatea spatiala: O(1)
"""
    def find_majority_element(nums):
        candidate = None
        count = 0
        
        for num in nums:
            if count == 0:
                candidate = num
                count = 1
            elif num == candidate:
                count += 1
            else:
                count -= 1

        count = 0
        for num in nums:
            if num == candidate:
                count += 1
        if count > len(nums) // 2:
            return candidate
        else:
            return None
"""