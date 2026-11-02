try:
    batas = int(input().strip())
    
    for i in range(1, batas + 1):
        if i % 2 != 0:
            print(i, end=" ")
    print()
    
    for i in range(batas, 1, -1):
        if i % 2 == 0:
            print(i, end=" ")
    print()
except ValueError:
    print("Input harus berupa bilangan bulat!")