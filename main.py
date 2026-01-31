# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.




# See PyCharm help at https://www.jetbrains.com/help/pycharm/

import matplotlib
matplotlib.use("Agg")  # GUI KULLANMAZ → parallel hatası OLMAZ

import matplotlib.pyplot as plt

# Test grafik
plt.plot([1, 2, 3], [4, 5, 6])
plt.title("Test Grafiği")
plt.xlabel("X")
plt.ylabel("Y")

# Grafiği dosyaya kaydet
plt.savefig("test_grafik.png")

# Belleği temizle
plt.close()


