global atoi
global itoh
global print
global fread
global exit
global next_line

section .text
; void write(char *text, int text_len)
; Write to STDOUT.
print:
    mov rax, 1
    mov rbx, rdi
    mov rcx, rsi
    mov rdi, 1
    mov rsi, rbx
    mov rdx, rcx
    syscall
    ret
; void exit()
; Exit with Code 0.
exit:
    mov rax, 0x3C
    mov rdi, 0
    syscall
    ret
; void fread(char *file, char *buffer, int count)
; Read file to buffer.
fread:
    push rdx
    push rsi
    mov rax, 2
    mov rsi, 0
    mov rdx, 0
    syscall
    mov rdi, rax
    mov rax, 0
    pop rsi
    pop rdx
    syscall
    mov rax, 0
    syscall
    ret
; int atoi(char *start, char *end)
; Converts string to integer from [start, end].
atoi:
    mov r10, 1
    mov rax, 0
    atoi_loop:
        cmp rsi, rdi
        jl atoi_done
        movzx rbx, byte [rsi]
        sub rbx, '0'
        imul rbx, r10
        add rax, rbx
        imul r10, 10
        sub rsi, 1
        jmp atoi_loop
    atoi_done:
    ret
; void itoh(int value, char *buffer)
; Converts integer value to hex string.
itoh:
    push 0
    itoh_convert_loop:
        mov r10, rdi
        and r10, 0xF
        cmp r10, 0xA
        jl itoh_less
        add r10, 7
        itoh_less:
        add r10, '0'
        push r10
        shr rdi, 4
        cmp rdi, 0
        je itoh_insert
        jmp itoh_convert_loop
    itoh_insert:
    mov DWORD [rsi], "0x"
    mov rax, 2
    itoh_insert_loop:
        pop rbx
        cmp rbx, 0
        je itoh_exit
        mov [rsi+rax], rbx
        add rax, 1 
        jmp itoh_insert_loop
    itoh_exit:
    ret
; char *next_line(char *start)
; Move pointer to next line.
next_line:
    mov rax, rdi
    next_line_loop:
        movzx rbx, byte [rax]
        cmp rbx, 0xA
        je next_line_done
        cmp rbx, 0
        je next_line_eof
        add rax, 1
        jmp next_line_loop
    next_line_eof:
    mov rax, 0
    ret
    next_line_done:
    add rax, 1
    ret
