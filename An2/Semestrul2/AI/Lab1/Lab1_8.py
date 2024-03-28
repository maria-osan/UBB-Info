"""
    Să se genereze toate numerele (în reprezentare binară) cuprinse
    între 1 și n. De ex. dacă n = 4, numerele sunt: 1, 10, 11, 100.
"""


# Complextatea temporala: O(n * logn)
# Complextatea spatiala: O(n * x),unde x este numarul de biti al celui mai mare numar din sir
def generare(n):
    sir = []
    for i in range(1, n+1):
        sir.append(bin(i)[2:])
    return sir


def test():
    assert (generare(4) == ['1', '10', '11', '100'])
    assert (generare(2) == ['1', '10'])
    assert (generare(7) == ['1', '10', '11', '100', '101', '110', '111'])


if __name__ == '__main__':
    test()

# Solutia oferita ce bot:
# Complextatea temporala: O(n)
# Complextatea spatiala: O(n)
"""
    from collections import deque
    
    def generate_binary_numbers(n):
        result = []
        queue = deque()
        queue.append('1')
    
        for _ in range(n):
            num = queue.popleft()
            result.append(num)
            queue.append(num + '0')
            queue.append(num + '1')
    
        return result
"""