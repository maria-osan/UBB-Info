"""
    Să se determine al k-lea cel mai mare element al unui
    șir de numere cu n elemente (k < n). De ex. al 2-lea cel
    mai mare element din șirul [7,4,6,3,9,1] este 7.
"""


# Complextatea temporala: O(n*logn)
# Complextatea spatiala: O(1)
def k_maxim(sir, k):
    sir.sort()
    return sir[len(sir) - k]


def test():
    assert (k_maxim([7, 4, 6, 3, 9, 1], 2) == 7)
    assert (k_maxim([7, 4, 6, 3, 9, 1], 5) == 3)


if __name__ == '__main__':
    test()

# Solutia oferita ce bot:
# Complextatea temporala: O(nlogk)
# Complextatea spatiala: O(k)
"""
    import heapq
    
    
    def kth_largest_element(arr, k):
        if k < 1 or k > len(arr):
            return None
        return heapq.nlargest(k, arr)[-1]
"""
