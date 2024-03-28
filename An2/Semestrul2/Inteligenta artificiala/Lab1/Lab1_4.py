"""
    Să se determine cuvintele unui text care apar exact o singură
    dată în acel text. De ex. cuvintele care apar o singură dată în
    ”ana are ana are mere rosii ana" sunt: 'mere' și 'rosii'.
"""


# Complextatea temporala: O(n)
# Complextatea spatiala: O(n)
def o_singura_aparitie(text):
    aparitii = {}
    for cuvant in text.split():
        aparitii[cuvant] = aparitii.get(cuvant, 0) + 1

    singura_aparitie = [cuvant for cuvant, aparitie in aparitii.items() if aparitie == 1]
    return singura_aparitie


def test():
    assert (o_singura_aparitie("ana are ana are mere rosii ana") == ['mere', 'rosii'])
    assert (o_singura_aparitie("ana are ana are ana") == [])
    assert (o_singura_aparitie("cuvintele unice sunt") == ['cuvintele', 'unice', 'sunt'])


if __name__ == '__main__':
    test()

# Solutia oferita ce bot:
# Complextatea temporala: O(n)
# Complextatea spatiala: O(n)
"""
    def unique_words(text):
        unique_words = set()
        multiple_words = set()
    
        # Split the text into words
        words = text.split()
    
        # Identify words that appear two or more times
        for word in words:
            if word in unique_words:
                unique_words.remove(word)
                multiple_words.add(word)
            elif word not in multiple_words:
                unique_words.add(word)
    
        return unique_words
"""