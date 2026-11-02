#include <stdio.h>

int main() {
    int n, kelipatan;
    
    if (scanf("%d %d", &n, &kelipatan) == 2) {
        int total_keseluruhan = 0;
        
        for (int i = 1; i <= n; i++) {
            int baris_total = 0;
            
            for (int j = i; j >= 1; j--) {
                int hasil_kali = j * kelipatan;
                baris_total += hasil_kali;
                
                printf("(%d * %d)", j, kelipatan);
                if (j > 1) {
                    printf(" + ");
                }
            }
            
            printf(" = %d\n", baris_total);
            total_keseluruhan += baris_total;
        }
        
        printf("%d\n", total_keseluruhan);
        
    } else {
        printf("Format input salah!\n");
    }

    return 0;
}