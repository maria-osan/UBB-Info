bits 32 ; assembling for the 32 bits architecture

; declare the EntryPoint (a label defining the very first instruction of the program)
global start        

; declare external functions needed by our program
extern exit               ; tell nasm that exit exists even if we won't be defining it
import exit msvcrt.dll    ; exit is a function that ends the calling process. It is defined in msvcrt.dll
                          ; msvcrt.dll contains exit, printf and all the other important C-runtime specific functions

; a, b, c, d - byte, e, f, g, h - word
segment data use32 class=data
    a db 2
    b db 2
    c db 3
    d db 3
    e dw 4
    h dw 1

; 12. (a * d + e) / [c + h / (c - b)]
segment code use32 class=code
    start:
        ; a * d
        mov al, [a]
        mov ah, [d]
        mul ah  ; ax = ah * ah = a * d
        
        ; a * d + e
        add ax, [e] ; ax = a * d + e
        
        mov bx,ax
        
        ; c - b
        mov al, [c]
        sub al, [b] ; al = c - b
        
        mov cl, al
        
        ; h / (c - b)
        mov ax, [h]
        div cl  ; ax / cl - al = h / (c - b), ah -rest
        
        ; c + h / (c - b)
        add al, [c] ; al = c + h / (c - b)
        
        mov dl, al
        
        ; (a * d + e) / [c + h / (c - b)]
        mov ax, bx
        div dl  ; al = ax / dl = (a * d + e) / [c + h / (c - b)], ah = (a * d + e) % [c + h / (c - b)]
    
        ; exit(0)
        push    dword 0      ; push the parameter for exit onto the stack
        call    [exit]       ; call exit to terminate the program
