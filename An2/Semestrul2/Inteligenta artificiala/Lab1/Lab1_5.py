"""
    Pentru un șir cu n elemente care conține valori din mulțimea {1, 2, ..., n - 1}
    astfel încât o singură valoare se repetă de două ori, să se identifice acea
    valoarecare se repetă. De ex. în șirul [1,2,3,4,2] valoarea 2 apare de două ori.
"""


# Complextatea temporala: O(n)
# Complextatea spatiala: O(n)
def duplicat(sir):
    n = len(sir)
    fr = [0] * (n + 1)  # vector de frecventa

    for i in sir:
        fr[i] += 1
        if fr[i] >= 2:
            return i


def test():
    assert (duplicat([1, 2, 3, 4, 2]) == 2)
    assert (duplicat([1, 2, 1, 3, 4]) == 1)
    assert (duplicat([2, 1, 2]) == 2)
    assert (duplicat([1, 1]) == 1)


if __name__ == '__main__':
    test()

# Solutia oferita ce bot:
# Complextatea temporala: O(n)
# Complextatea spatiala: O(n)
"""
    def gaseste_repetare_set(nums):
        aparitii = set()
        for num in nums:
            if num in aparitii:
                return num
            else:
                aparitii.add(num)
"""