try:
    data = input().split()
    a = int(data[0])
    b = int(data[1])
    
    if a < b:
        i = a
        j = b
        while i <= b and j >= a:
            print(f"{i} {j}", end="")
            i += 1
            j -= 1
            if i <= b and j >= a:
                print(" - ", end="")
        print()
    else:
        i = a
        j = b
        while i >= b and j <= a:
            print(f"{i} {j}", end="")
            i -= 1
            j += 1
            if i >= b and j <= a:
                print(" - ", end="")
        print()
except (IndexError, ValueError):
    print("Format input harus berupa dua buah angka!")