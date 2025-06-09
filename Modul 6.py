#DESIMAL KE BINER
def proses_desimal_ke_biner(n):
    hasil = []
    asli = n
    while n > 0:
        hasil.append(str(n % 2))
        print(f"{n} ÷ 2 = {n // 2} sisa {n % 2}")
        n //= 2
    hasil.reverse()
    print(f"\nHasil biner dari {asli} adalah: {''.join(hasil)}")

#DESIMAL KE OKTAL
def proses_desimal_ke_oktal(n):
    hasil = []
    asli = n
    while n > 0:
        hasil.append(str(n % 8))
        print(f"{n} ÷ 8 = {n // 8} sisa {n % 8}")
        n //= 8
    hasil.reverse()
    print(f"\nHasil oktal dari {asli} adalah: {''.join(hasil)}")

#DESIMAL KE HEKSA
def proses_desimal_ke_heksa(n):
    simbol = "0123456789ABCDEF"
    hasil = []
    asli = n
    while n > 0:
        sisa = n % 16
        hasil.append(simbol[sisa])
        print(f"{n} ÷ 16 = {n // 16} sisa {sisa} ({simbol[sisa]})")
        n //= 16
    hasil.reverse()
    print(f"\nHasil heksadesimal dari {asli} adalah: {''.join(hasil)}")

#BINER KE DESIMAL
def proses_biner_ke_desimal(biner):
    biner = biner[::-1]
    total = 0
    print("\nLangkah-langkah:")
    for i in range(len(biner)):
        nilai = int(biner[i]) * (2 ** i)
        print(f"{biner[i]} × 2^{i} = {nilai}")
        total += nilai
    print(f"Hasil desimal: {total}")

#OKTAL KE DESIMAL
def proses_oktal_ke_desimal(oktal):
    oktal = oktal[::-1]
    total = 0
    print("\nLangkah-langkah:")
    for i in range(len(oktal)):
        nilai = int(oktal[i]) * (8 ** i)
        print(f"{oktal[i]} × 8^{i} = {nilai}")
        total += nilai
    print(f"Hasil desimal: {total}")

#HEKSA KE DESIMAL
def proses_heksa_ke_desimal(heksa):
    heksa = heksa[::-1].upper()
    simbol = "0123456789ABCDEF"
    total = 0
    print("\nLangkah-langkah:")
    for i in range(len(heksa)):
        nilai = simbol.index(heksa[i]) * (16 ** i)
        print(f"{heksa[i]} × 16^{i} = {nilai}")
        total += nilai
    print(f"Hasil desimal: {total}")

# Menu
while True:
    print("\n=== KONVERSI BILANGAN ===")
    print("1. Desimal ke Biner")
    print("2. Desimal ke Oktal")
    print("3. Desimal ke Heksadesimal")
    print("4. Biner ke Desimal")
    print("5. Oktal ke Desimal")
    print("6. Heksadesimal ke Desimal")
    print("7. Keluar")

    pilihan = input("Pilih menu (1-7): ")

    if pilihan == "1":
        n = int(input("Masukkan bilangan desimal: "))
        proses_desimal_ke_biner(n)
    elif pilihan == "2":
        n = int(input("Masukkan bilangan desimal: "))
        proses_desimal_ke_oktal(n)
    elif pilihan == "3":
        n = int(input("Masukkan bilangan desimal: "))
        proses_desimal_ke_heksa(n)
    elif pilihan == "4":
        b = input("Masukkan bilangan biner: ")
        proses_biner_ke_desimal(b)
    elif pilihan == "5":
        o = input("Masukkan bilangan oktal: ")
        proses_oktal_ke_desimal(o)
    elif pilihan == "6":
        h = input("Masukkan bilangan heksadesimal: ")
        proses_heksa_ke_desimal(h)
    elif pilihan == "7":
        print("Terima kasih!")
        break
    else:
        print("Pilihan tidak valid.")
