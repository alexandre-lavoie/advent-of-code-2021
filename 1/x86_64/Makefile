build:
	nasm -felf64 task1.asm
	nasm -felf64 task2.asm
	nasm -felf64 utils.asm
	ld utils.o task1.o -o task1
	ld utils.o task2.o -o task2
clean:
	rm *.o task1 task2
