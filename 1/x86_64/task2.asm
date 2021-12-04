global _start

extern atoi
extern itoh
extern fread
extern print
extern exit
extern next_line

section .data
file_content_size: equ 10000
file: db "../input.txt", 0
text: db "Task 2: ", 0
text_len: equ $-text

section .bss
fptr: resb 8
file_content: resb file_content_size
queue: resb 24
output: resb 8

section .text
_start:
mov rdi, text
mov rsi, text_len
call print

mov DWORD [fptr], file_content
mov rdi, file
mov rsi, file_content
mov rdx, file_content_size
call fread

mov r11, 0 ; Offset
mov r12, 0 ; Count
mov r13, 0 ; Sum
main_loop:
    ; Next Number
    mov rdi, [fptr]
    call next_line
    cmp rax, 0
    je main_print
    mov [fptr], rax
    sub rax, 2
    mov rsi, rax
    call atoi
    ; Compare
    mov rcx, r13
    sub rcx, [queue+r11]
    add rcx, rax
    cmp r13, rcx 
    jge skip_count
    add r12, 1
    skip_count:
    mov [queue+r11], rax
    mov r13, rcx
    add r11, 8
    cmp r11, 24
    jne main_loop
    mov r11, 0
    jmp main_loop

main_print:
sub r12, 3
mov rdi, r12
mov rsi, output
call itoh
mov rdi, output
mov rsi, 5
call print
call exit
