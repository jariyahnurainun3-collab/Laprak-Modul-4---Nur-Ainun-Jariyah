#include <stdio.h>

int main() {
    int kelipatan;
    char simbol;

    if (scanf("%d %c", &kelipatan, &simbol) == 2) {
        
        for (int i = 1; i <= 50; i++) {
            
            if (i % kelipatan == 0) {
                printf("%c ", simbol);
            } else {
                printf("%d ", i);
            }
        }
        printf("\n"); 
    } else {
        printf("Format input salah! Masukkan contoh: 6 *\n");
    }

    return 0;
}