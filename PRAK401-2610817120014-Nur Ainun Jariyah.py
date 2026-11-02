try:
    user_input = input().strip()
    if user_input:
        input_data = user_input.split()
        kelipatan = int(input_data[0])
        simbol = input_data[1]
        
        for i in range(1, 51):
            if i % kelipatan == 0:
                print(simbol, end=" ")
            else:
                print(i, end=" ")
        print() 
except (IndexError, ValueError):
    print("Format input harus berupa: [angka_kelipatan] [spasi] [simbol], contoh: 6 *")