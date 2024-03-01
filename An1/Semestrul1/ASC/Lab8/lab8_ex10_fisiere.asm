bits 32 

global start        

extern exit, fopen, fprintf, fclose, gets, printf
import exit msvcrt.dll  
import fopen msvcrt.dll  
import fprintf msvcrt.dll
import fclose msvcrt.dll
import gets msvcrt.dll
import printf msvcrt.dll

; our data is declared here 
segment data use32 class=data
    nume_fisier times 30 db 0  
    mesaj_fisier db "Dati numele fisierului: ", 0
    mod_acces db "w", 0          ; modul de deschidere a fisierului: w - pentru scriere. daca fiserul nu exista, se va crea      
    text times 120 db 0 
    mesaj_text db "Dati textul: ", 0
                                    
    descriptor_fis dd -1         ; variabila in care vom salva descriptorul fisierului - necesar pentru a putea face referire la fisier
                                    
; 10. Sa se citeasca de la tastatura un nume de fisier si un text. Sa se creeze un fisier cu numele dat in directorul curent si sa se scrie textul in acel fisier. Observatii: Numele de fisier este de maxim 30 de caractere. Textul este de maxim 120 de caractere.
segment code use32 class=code
    start: 
        push dword mesaj_fisier
        call [printf]
        add esp, 4
        
        push dword nume_fisier
        call [gets]
        add esp, 4
        
        ; apelam fopen pentru a crea fisierul
        push dword mod_acces     
        push dword nume_fisier
        call [fopen]
        add esp, 4*2                

        mov [descriptor_fis], eax   
        
        ; verificam daca functia fopen a creat cu succes fisierul 
        cmp eax, 0
        je final
        
        ; citim textul
        push dword mesaj_text
        call [printf]
        add esp, 4
        
        push dword text
        call [gets]
        add esp, 4
        
        ; scriem textul in fisierul deschis folosind functia fprintf
        push dword text
        push dword [descriptor_fis]
        call [fprintf]
        add esp, 4*2
        
        ; apelam functia fclose pentru a inchide fisierul
        push dword [descriptor_fis]
        call [fclose]
        add esp, 4
        
      final:
        
        ; exit(0)
        push    dword 0      ; push the parameter for exit onto the stack
        call    [exit]       ; call exit to terminate the program       