# Pembagian dengan rekursif

# 12 / 3 = 12 - 3 - 3 - 3 sampai nilainya > 0
def pembagian(a, b):
    
    # basis
    if a == b:
        return 1
    
    if a < b:
        return 0
    
    return 1 + pembagian(a-b, b)


print(pembagian(6,3))