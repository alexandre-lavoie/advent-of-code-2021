#include <stdio.h>
#include <strings.h>

#define INPUT_FILE "../input.txt"

int task1() {
    FILE *fd = fopen(INPUT_FILE, "r");

    int x, z = 0;

    char label[16];
    int count;
    while(fscanf(fd, "%s %d", label, &count) != EOF) {
        switch(label[0]) {
            case 'u':
                z -= count;
                break;
            case 'd':
                z += count;
                break;
            case 'f':
                x += count;
                break;
        }
    }
    fclose(fd);

    return x * z;
}

int task2() {
    FILE *fd = fopen(INPUT_FILE, "r");

    int x, y, z = 0;

    char label[16];
    int count;
    while(fscanf(fd, "%s %d", label, &count) != EOF) {
        switch(label[0]) {
            case 'u':
                z -= count;
                break;
            case 'd':
                z += count;
                break;
            case 'f':
                x += count;
                y += z * count;
                break;
        }
    }
    fclose(fd);

    return x * y;
}

int main() {
    printf("Task 1: %d\n", task1());
    printf("Task 2: %d\n", task2());
    return 0;
}