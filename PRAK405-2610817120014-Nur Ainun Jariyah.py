try:
    data = input().split()
    n = int(data[0])
    kelipatan = int(data[1])
    
    total_keseluruhan = 0
    
    for i in range(1, n + 1):
        baris_total = 0
        
        for j in range(i, 0, -1):
            hasil_kali = j * kelipatan
            baris_total += hasil_kali
            
            print(f"({j} * {kelipatan})", end="")
            if j > 1:
                print(" + ", end="")
        
        print(f" = {baris_total}")
        total_keseluruhan += baris_total
        
    print(total_keseluruhan)

except (IndexError, ValueError):
    print("Format input harus berupa dua buah angka!")