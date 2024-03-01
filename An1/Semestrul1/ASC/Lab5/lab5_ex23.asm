bits 32 

global start        

extern exit              
import exit msvcrt.dll    

; s - sir de octeti
segment data use32 class=data
    s db 1, 4, 2, 4, 8, 2, 1, 1 ; declararea sirului initial s
    len equ $-s ; stabilirea lungimea sirului initial 
    d times len db 0    ; rezervarea unui spatiu de dimensiune len pentru sirul destinatie d si initializarea acestuia
    

; 23. Se da un sir de octeti S. 
; Sa se obtina in sirul D multimea elementelor din S.
; ex: S: 1, 4, 2, 4, 8, 2, 1, 1
;     D: 1, 4, 2, 8
segment code use32 class=code
    start:
        mov ecx, len    ; punem lungimea in ECX pentru a putea realiza bucla loop de ecx ori
        mov esi, 0
        mov edi, 0
        jecxz final
        
        repeta:
            mov al, [s+esi]
            push ecx
            mov ecx, edi
            jecxz continuare
            
            executa:
                cmp al, [d+ecx]
                je next ; al == [d+edi]
            loop executa
            
            continuare:
                mov [d+edi], al
                inc edi
            
            next:
            inc esi
            pop ecx
        loop repeta
        
        final:  ; terminarea programului
    
        ; exit(0)
        push    dword 0      ; push the parameter for exit onto the stack
        call    [exit]       ; call exit to terminate the program
