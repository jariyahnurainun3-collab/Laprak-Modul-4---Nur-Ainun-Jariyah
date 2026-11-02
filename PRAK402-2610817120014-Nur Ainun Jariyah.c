#include <stdio.h>

int main() {
    int batas;

    if (scanf("%d", &batas) == 1) {
        
        for (int i = 1; i <= batas; i++) {
            if (i % 2 != 0) {
                printf("%d ", i);
            }
        }
        printf("\n");

        for (int i = batas; i >= 2; i--) {
            if (i % 2 == 0) {
                printf("%d ", i);
            }
        }
        printf("\n");
        
    } else {
        printf("Format input salah!\n");
    }

    return 0;
}