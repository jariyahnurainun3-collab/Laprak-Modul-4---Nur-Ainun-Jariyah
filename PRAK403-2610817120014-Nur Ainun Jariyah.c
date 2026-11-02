#include <stdio.h>

int main() {
    int a, b;

    if (scanf("%d %d", &a, &b) == 2) {
        
        if (a < b) {
            int i = a, j = b;
            while (i <= b && j >= a) {
                printf("%d %d", i, j);
                i++;
                j--;
                if (i <= b && j >= a) {
                    printf(" - ");
                }
            }
        } 
        else {
            int i = a, j = b;
            while (i >= b && j <= a) {
                printf("%d %d", i, j);
                i--;
                j++;
                if (i >= b && j <= a) {
                    printf(" - ");
                }
            }
        }
        printf("\n");
    } else {
        printf("Format input salah!\n");
    }

    return 0;
}