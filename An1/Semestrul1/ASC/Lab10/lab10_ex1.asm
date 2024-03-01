bits 32
global start

extern exit, scanf, printf
import exit msvcrt.dll
import scanf msvcrt.dll
import printf msvcrt.dll

segment data use32 class=data
    format db "%d", 0
    numar dd 0
    mesaj db "Dati un numar: ", 0
    zexe dw 10

; Scrieti un program care citeste un numar natural n de la tastatura si afiseaza numarul de cifre a lui n in baza 10.
segment code use32 class=code
    start:
        push dword mesaj
        call [printf]
        add esp, 4
            
        ;scanf (format, &n)
        push dword numar
        push dword format
        call [scanf]
        add esp, 2*4
        
        mov eax, [numar]
        mov ebx, 0
        
        repeta:
            inc ebx
            div word [zece]
            
            cmp ax, 0
            je afara
            
            
        
        jmp repeta
        
    afara:
    
        push dword numar
        push dword format
        call [printf]
        add esp, 2*4
    
        ; exit(0)
        push dword 0        ; push the parameter for exit onto the stack
        call [exit]         ; call exit to terminate the program
