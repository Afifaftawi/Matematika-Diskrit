angka_desimal = 95
biner_awal = bin(angka_desimal)
oktal_awal = oct(angka_desimal)
heksadesimal_awal = hex(angka_desimal)
biner_tanpa_awalan = biner_awal[2:]
oktal_tanpa_awalan = oktal_awal[2:]
heksadesimal_tanpa_awalan = heksadesimal_awal[2:].upper()  

print("=== KONVERSI BILANGAN DESIMAL ===")
print("Angka Desimal     :", angka_desimal)
print("Dalam Biner       :", biner_tanpa_awalan)
print("Dalam Oktal       :", oktal_tanpa_awalan)
print("Dalam Heksadesimal:", heksadesimal_tanpa_awalan)
