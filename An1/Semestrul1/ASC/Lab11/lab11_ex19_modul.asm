bits 32

global sir_negativ

segment code use32 cod

sir_negativ:

    sir_neg:
        lodsd
        cmp eax, 0
        jge pozitiv
        stosd
    
        pozitiv:
        loop sir_neg
    
    final:
    ret 
