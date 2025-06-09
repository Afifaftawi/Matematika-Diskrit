def desimal_ke_basis(n, basis):
    simbol = "0123456789ABCDEF"
    if n == 0:
        print("Hasil: 0")
        return
    hasil = ""
    asli = n
    while n > 0:
        sisa = n % basis
        print(f"{n} ÷ {basis} = {n // basis} sisa {sisa} ({simbol[sisa]})" if basis==16 else f"{n} ÷ {basis} = {n // basis} sisa {sisa}")
        hasil = simbol[sisa] + hasil
        n //= basis
    print(f"Hasil dari {asli} adalah: {hasil}")

def basis_ke_desimal(num_str, basis):
    simbol = "0123456789ABCDEF"
    num_str = num_str.upper()
    total = 0
    print("Langkah-langkah:")
    for i, digit in enumerate(reversed(num_str)):
        nilai = simbol.index(digit) * (basis ** i)
        print(f"{digit} × {basis}^{i} = {nilai}")
        total += nilai
    print(f"Hasil desimal: {total}")

while True:
    print("\nMenu:")
    print("1. Desimal ke Biner")
    print("2. Desimal ke Oktal")
    print("3. Desimal ke Heksadesimal")
    print("4. Biner ke Desimal")
    print("5. Oktal ke Desimal")
    print("6. Heksadesimal ke Desimal")
    print("7. Keluar")

    pilihan = input("Pilih (1-7): ")

    if pilihan == "1":
        n = int(input("Masukkan desimal: "))
        desimal_ke_basis(n, 2)
    elif pilihan == "2":
        n = int(input("Masukkan desimal: "))
        desimal_ke_basis(n, 8)
    elif pilihan == "3":
        n = int(input("Masukkan desimal: "))
        desimal_ke_basis(n, 16)
    elif pilihan == "4":
        b = input("Masukkan biner: ")
        basis_ke_desimal(b, 2)
    elif pilihan == "5":
        o = input("Masukkan oktal: ")
        basis_ke_desimal(o, 8)
    elif pilihan == "6":
        h = input("Masukkan heksadesimal: ")
        basis_ke_desimal(h, 16)
    elif pilihan == "7":
        print("Terima kasih!")
        break
    else:
        print("Pilihan salah.")
