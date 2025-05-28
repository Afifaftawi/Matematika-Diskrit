import numpy as np

#mendefinisikan fungsi
def f(x):
  return x**2 - 4

#mencari akar-akar dari f(X) = 0
akar = np.roots ([1, 0, -4])#koefisien dari x^2,x^1,dan konstanta

#menampilkan hasil
print("akar-akar dari f(x) = x^2 - 4 adalah:",akar)

import numpy as np
import matplotlib.pyplot as plt

#definisikan fungsi
def f(x):
  return x**2 - 4

#cari akar-akar fungsi (akar dari persamaan x^2 4 =0)
akar = np.roots ([1,0,-4])


#generate nilai x dari -3 hingga 3
x = np.linspace (-3,3,400) #400 titik
y = f(x)

#plot grafik
plt.figure(figsize=(8,5))
plt.plot(x, y, label='$f(x) = x^2 - 4$', color = 'purple')
plt.title("grafik fungsi kuadrat")
plt.xlabel("f(x)")
plt.grid(True)
plt.legend()
