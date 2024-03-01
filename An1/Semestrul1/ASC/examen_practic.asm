bits 32 ; assembling for the 32 bits architecture

global start        

extern exit, scanf, fscanf, printf, fopen, fclose
import exit msvcrt.dll
import scanf msvcrt.dll
import fscanf msvcrt.dll
import printf msvcrt.dll
import fopen msvcrt.dll
import fclose msvcrt.dll


segment data use32 class=data
    N dd 0
    format_n db "%d", 0
    mesaj_n db "n= ", 0
    nume_fisier db "date.txt", 0
    format_fisier db "%s", 0
    mesaj_fiser db "Dati numele fisierului: ", 0
    mod_acces db "r", 0
    descriptor_fis dd -1
    numar dd 0
    format_afisare db "%d ", 0

; Să se scrie un program în limbaj de asamblare care:
; citește de la tastatură un număr natural N (0 < N < 10) și numele unui fișier text;
; citește toate numerele întregi din fișierul dat;
; afișează pe ecran doar numerele întregi POZITIVE și care sunt divizibile cu N.
; Fișierul text trebuie să existe și va conține doar numere întregi separate prin spații
segment code use32 class=code
    start:
        ; citesc numarul N
        ; printf(mesaj_n)
        push dword mesaj_n
        call [printf]
        add esp, 4
        
        ; scanf(format_n, &N)
        push dword N
        push dword format_n
        call [scanf]
        add esp, 4*2
        
        ; citesc numele unui fisier
        ; printf(mesaj_fiser)
        push dword mesaj_fiser
        call [printf]
        
        ; scanf(format_fisier, &nume_fisier)
        push dword nume_fisier
        push dword format_fisier
        call [scanf]
        add esp, 4*2
        
        ; deschid fisierul
        ; fopen(nume_fisier, mod_acces)
        push dword mod_acces
        push dword nume_fisier
        call [fopen]
        add esp, 4*2
        
        mov [descriptor_fis], eax
        
        cmp eax, 0
        je final
        
    citire:
        ; citesc numarul din fisier
        ; fscanf(descriptor_fis, format_n, &numar)
        push dword numar
        push dword format_n
        push dword [descriptor_fis]
        call [fscanf]
        add esp, 4*3
        
        ; prelucrez numarul
        push eax
        
        cmp dword [N], 0
        jl next
        mov eax, dword [numar]
        mov edx, 0
        div dword [N]
        
        cmp edx, 0
        jne next
        
        ; afisez numarul pe ecran
        ; printf(format_afisare, numar)
        push dword [numar]
        push dword format_afisare
        call [printf]
        add esp, 4*2
        
        next:
        pop eax
        
        cmp eax, 1
        jne afara
        
        jmp citire
        
    afara:
        ; inchid fisierul
        ; fclose(descriptor_fis)
        push dword [descriptor_fis]
        call [fclose]
        add esp, 4
    
    final:
    
        ; exit(0)
        push    dword 0      ; push the parameter for exit onto the stack
        call    [exit]       ; call exit to terminate the program
