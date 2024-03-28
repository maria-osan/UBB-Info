"""
    Să se determine ultimul (din punct de vedere alfabetic) cuvânt care
    poate apărea într-un text care conține mai multe cuvinte separate
    prin ” ” (spațiu). De ex. ultimul (dpdv alfabetic) cuvânt din
    ”Ana are mere rosii si galbene” este cuvântul "si".
"""


# Complextatea temporala: O(n)
# Complextatea spatiala: O(n)
def ultimul_cuv_alfabetic(text):
    cuvinte = text.split(" ")
    ultimul = ""
    for cuv in cuvinte:
        if ultimul < cuv:
            ultimul = cuv
    return ultimul


def test():
    assert (ultimul_cuv_alfabetic("Ana are mere rosii si galbene") == "si")
    assert (ultimul_cuv_alfabetic("ana are ana are mere rosii ana") == "rosii")
    assert (ultimul_cuv_alfabetic("A C B 1 E 2") == "E")


if __name__ == '__main__':
    test()

# Solutia oferita ce bot:
# Complextatea temporala: O(n)
# Complextatea spatiala: O(1)
"""
    def last__word(text):
        last = ''
        word = ''
        for character in text:
            if character != ' ':
                word += character
            else:
                if word > last:
                    last = word
                word = ''
        # Check the last word
        if word > last:
            last = word
        return last
"""