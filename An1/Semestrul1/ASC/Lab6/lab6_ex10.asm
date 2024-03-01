bits 32 
global start        

extern exit               
import exit msvcrt.dll    

segment data use32 class=data
    a dw 1234h, 67abh, 89cdh
    len equ ($-a)/2
    b1 times len db 0
    b2 times len db 0

; 10. Se da un sir A de cuvinte. Construiti doua siruri de octeti  
; - B1: contine ca elemente partea superioara a cuvintelor din A
; - B2: contine ca elemente partea inferioara a cuvintelor din A
segment code use32 class=code
    start:
        mov ecx, len
        jecxz final
        cld
        mov esi, a
        mov edi, b1
        
        repeta:
            lodsb
            lodsb
            stosb
        
        loop repeta
        
        mov ecx, len
        jecxz final
        cld
        mov esi, a
        mov edi, b2
        
        Repeta:
            lodsw
            stosb
        
        loop Repeta
        
        final:
    
        ; exit(0)
        push    dword 0      ; push the parameter for exit onto the stack
        call    [exit]       ; call exit to terminate the program
