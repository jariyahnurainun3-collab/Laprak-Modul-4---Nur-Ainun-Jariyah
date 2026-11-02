while True:
    print("Pilih program")
    print("1. Penjumlahan")
    print("2. Pengurangan")
    print("3. Perkalian")
    print("4. Pembagian")
    print("5. Exit")
    
    try:
        pilihan = int(input("Masukkan Pilihan : "))
        
        if pilihan == 5:
            print("Terimakasih, telah menggunakan Kalkulator Nur Ainun Jariyah")
            break
        elif pilihan >= 1 and pilihan <= 4:
            n1 = float(input("Masukkan nilai pertama : "))
            n2 = float(input("Masukkan nilai kedua : "))
            
            if pilihan == 1:
                hasil = n1 + n2
                print(f"Hasil Penjumlahan antara {n1:.2f} dengan {n2:.2f} adalah {hasil:.2f}")
            elif pilihan == 2:
                hasil = n1 - n2
                print(f"Hasil Pengurangan antara {n1:.2f} dengan {n2:.2f} adalah {hasil:.2f}")
            elif pilihan == 3:
                hasil = n1 * n2
                print(f"Hasil Perkalian antara {n1:.2f} dengan {n2:.2f} adalah {hasil:.2f}")
            elif pilihan == 4:
                if n2 == 0:
                    print("Error: Pembagian dengan nol tidak diperbolehkan.")
                else:
                    hasil = n1 / n2
                    print(f"Hasil Pembagian antara {n1:.2f} dengan {n2:.2f} adalah {hasil:.2f}")
        else:
            print("Input anda salah, silahkan coba lagi")
            
    except ValueError:
        print("Input anda salah, silahkan coba lagi")