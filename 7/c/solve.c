#include <stdio.h>

#define IN_FILE "../input.txt"
#define BUFF_SIZE 2048
#define abs(a) ((a) >= 0 ? (a) : -(a))
#define max(a, b) ((a) > (b) ? (a) : (b))
#define min(a, b) ((a) < (b) ? (a) : (b))

int main() {
    FILE *file = fopen(IN_FILE, "r");

    int h[BUFF_SIZE];
    int l = 0;
    while(fscanf(file, "%d,", h + l) != EOF){l++;}
    fclose(file);

    int x = 0;
    int n = __INT_MAX__;
    for(int i = 0; i < l; i++) {
        x = max(h[i], x);
        n = min(h[i], n);
    }

    int t1 = __INT_MAX__;
    int t2 = __INT_MAX__;
    for(int i = n; i <= x; i++) {
        int lt1 = 0;
        int lt2 = 0;

        for(int j = 0; j < l; j++) {
            int d = abs(h[j] - i);
            lt1 += d;
            lt2 += (d * (d + 1)) / 2;
        }

        t1 = min(t1, lt1);
        t2 = min(t2, lt2);
    }

    printf("Task 1: %d\n", t1);
    printf("Task 2: %d\n", t2);

    return 0;
}
