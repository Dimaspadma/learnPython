# Ada 3 cara :

# Cara Pertama : dengan variable sementara
def swapWithTmp(x, y):
  tmp = x
  x = y
  y = tmp


# Cara Kedua: Tanpa variable sementara
def swapPython(x, y):
  x, y = y, x

# Cara Ketiga dengan aritmatika
def swapA:
# Perjumlah dan Pengurangan
x = 12
y = 8

x = x + y
y = x - y
x = x - y

# print(x, y)

# Perkalian dan Pembagian
x = 6
y = 3

x = x * y
y = x / y
x = x / y

# print(x, y)

#%% Menggunakan XOR
# for integer only
x = 5
y = 21

x = x ^ y
y = x ^ y
x = x ^ y

print(x, y)