bits 32 ; assembling for the 32 bits architecture

global start        

extern exit, fopen, fclose, printf, fscanf
import exit msvcrt.dll  
import fopen msvcrt.dll  
import fclose msvcrt.dll
import printf msvcrt.dll
import fscanf msvcrt.dll

extern sir_negativ

segment data use32 class=data public
    nume_fisier db "numere.txt", 0
    mod_acces db "r", 0          ; modul de deschidere a fisierului: r - pentru citire. fisierul trebuie sa existe
    
    descriptor_fis dd -1
    
    n dd 0
    N times 50 dd 0
    P times 50 dd 0
    lenP dd 0
    sir times 50 dd 0
    len_sir dd 0
    
    format db "%d", 0
    format2 db "%d ", 0
    
    mesaj_pozitive db "Numerele pozitive sunt: ", 0
    mesaj_negative db "Numerele negative sunt: ", 0

; 19. Se citesc din fisierul numere.txt mai multe numere (pozitive si negative). Sa se creeze 2 siruri rezultat N si P astfel: N - doar numere negative si P - doar numere pozitive. Afisati cele 2 siruri rezultate pe ecran.
segment code use32 class=code public
    start:
        ; fopen(nume_fisier, mod_acces)
        push dword mod_acces
        push dword nume_fisier
        call [fopen]
        add esp, 2*4
        
        mov [descriptor_fis], eax
        
        cmp eax, 0
        je final
        
        mov esi, 0
        mov edi, 0
        
    citire:
        ; citire numar
        ; fscanf(descriptor_fis, format, &n)
        push dword n
        push dword format
        push dword [descriptor_fis]
        call [fscanf]
        add esp, 3*4
        
        mov ebx, [n]
        
        mov [sir + esi], ebx
        add esi, 4
        add dword [len_sir], 1

        cmp eax, 1
        jne afara
        
        jmp citire
        
    afara:
        sub dword [len_sir], 1

        mov edi, P
        mov esi, sir
        mov ecx, [len_sir]
        jecxz next
        cld
        
        sir_poz:
            lodsd
            cmp eax, 0
            jl negativ
            stosd
            add dword [lenP], 1
        
            negativ:
            loop sir_poz
            
    next:
        
        push dword mesaj_pozitive
        call [printf]
        add esp, 1*4
        
        mov ecx, [lenP]
        cld
        mov esi, P
        
        afisareP:
            push ecx
            lodsd
            push eax
            push dword format2
            call [printf]
            add esp, 2*4
            pop ecx
            
            loop afisareP
            
        mov edi, N
        mov esi, sir
        mov ecx, [len_sir]
        jecxz final
        cld
        call sir_negativ
        
        push dword mesaj_negative
        call [printf]
        add esp, 1*4
         
        mov ecx, [len_sir]
        sub ecx, [lenP]
        cld
        mov esi, N
        
        afisareN:
            push ecx
            lodsd
            push eax
            push dword format2
            call [printf]
            add esp, 2*4
            pop ecx
            
            loop afisareN
        
        ; fclose(descriptor_fis)
        push dword [descriptor_fis]
        call [fclose]
        add esp, 4
        
    final:
    
        ; exit(0)
        push    dword 0      ; push the parameter for exit onto the stack
        call    [exit]       ; call exit to terminate the program
