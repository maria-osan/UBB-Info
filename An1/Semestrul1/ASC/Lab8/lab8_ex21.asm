bits 32 

global start        

extern exit, scanf, printf
import exit msvcrt.dll
import scanf msvcrt.dll
import printf msvcrt.dll  

; our data is declared here 
segment data use32 class=data
    format db "%d", 0
    a dw 0
    b dw 0
    c dd 0
    format_c db "Numarul obtinut in baza 16 este: %x ", 0
    mesaj_a db "Dati numarul a: ", 0
    mesaj_b db "Dati numarul b: ", 0

; 21. Sa se citeasca de la tastatura doua numere a si b de tip word. Sa se afiseze in baza 16 numarul c de tip dword pentru care partea  low este suma celor doua numere, iar partea high este diferenta celor doua numere. Exemplu:
; a = 574, b = 136
; c = 01B602C6h
segment code use32 class=code
    start:
        push dword mesaj_a
        call [printf]
        add esp, 4
        
        ;scanf (format, &a)
        push dword a
        push dword format
        call [scanf]
        add esp, 2*4
        
        push dword mesaj_b
        call [printf]
        add esp, 4
        
        ;scanf (format, &b)
        push dword b
        push dword format
        call [scanf]
        add esp, 2*4
        
        ; a + b
        mov ax, [a]
        add ax, [b]
        
        ; a - b
        mov dx, [a]
        sub dx, [b]
        
        ; c = a-b : a+b
        push dx
        push ax
        pop eax
        
        mov dword [c], eax
        
        ; afisare
        push dword [c]
        push dword format_c
        call [printf]
        add esp, 2*4
    
        ; exit(0)
        push    dword 0      ; push the parameter for exit onto the stack
        call    [exit]       ; call exit to terminate the program
