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
text: db "Task 1: ", 0
text_len: equ $-text

section .bss
fptr: resb 8
file_content: resb file_content_size
count: resb 8
previous: resb 8
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
    cmp rax, [previous]
    jl less
    add DWORD [count], 1
    less:
    mov [previous], rax
    jmp main_loop
main_print:
sub DWORD [count], 1
mov rdi, [count]
mov rsi, output
call itoh
mov rdi, output
mov rsi, 5
call print
call exit
