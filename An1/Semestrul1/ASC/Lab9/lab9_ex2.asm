bits 32
global start

extern exit, scanf, printf
import exit msvcrt.dll
import scanf msvcrt.dll
import printf msvcrt.dll

segment data use32 class=data
    numere times 100 dd 0
    format db "%d", 0
    n dd 0
    mesaj db "Dati un numar: ", 0
    format2 db "%d ", 0
    
; Cititi de la tastatura si afisati un sir de numere intregi.
; (citirea se termina atunci cand utilizatorul introduce numarul ZERO)
segment code use32 class=code
    start:
        cld
        mov edi, numere
        mov ebx, 0
        
        repeta:
            push dword mesaj
            call [printf]
            add esp, 4
            
            ;scanf (format, &n)
            push dword n
            push dword format
            call [scanf]
            add esp, 2*4
            
            ; stocam n in sir
            mov eax, [n]
            cmp eax, 0
            je afara
            stosd
            inc ebx
        
        jmp repeta
        
        afara:
        mov ecx, ebx
        cld
        mov esi, numere
        
        afisare:
            push ecx
            lodsd
            push eax
            push dword format2
            call [printf]
            add esp, 2*4
            pop ecx
        
        loop afisare
    
        ; exit(0)
        push dword 0        ; push the parameter for exit onto the stack
        call [exit]         ; call exit to terminate the program
