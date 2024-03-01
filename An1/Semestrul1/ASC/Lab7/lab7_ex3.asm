bits 32
global start

extern exit
import exit msvcrt.dll

segment data use32 class=data
    s1 dw 1234h, 67abh, 89cdh
    len equ $-s1
    s2 dw 2345h, 5678h, 4567h
    d times len dw 0

; Se dau doua siruri de cuvinte s1 si s2.
; Se cere sirul de cuvinte d obtinut in interpretarea cu semn, astfel:
; - d[i] = s1[i], daca s1[i] > s2[i]
; - d[i] = s2[i], altfel.
segment code use32 class=code
    start:
        mov ecx, len
        jecxz final
        
        cld
        mov esi, s1
        mov edi, d
        rep movsw
        
        mov ecx, len
        cld
        mov esi, s2
        mov edi, d
        repeta:
            cmpsw
            jle mai_mic
            
            sub esi, 2
            movsw
            
            mai_mic:
            
        loop repeta
        
        final:
    
        ; exit(0)
        push dword 0        ; push the parameter for exit onto the stack
        call [exit]         ; call exit to terminate the program
