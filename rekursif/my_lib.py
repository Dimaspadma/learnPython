def jumlah(a, b):
    if b == 0:
        return a

    return jumlah(a, b-1) + 1


def kurang(a, b):
    if b == 0:
        return a

    return kurang(a, b-1) - 1

def kali(a, b):
    if b == 1:
        return a

    elif b == 0:
        return 0
    
    elif b < 0:
        return -(a) + (kali(a, b+1))
    
    return a + kali(a, b-1)

def pow(a, b):
    if b == 1:
        return a
    
    elif b == 0:
        return 1
    
    elif b < 0:
        return 1 / (a * pow(a, b+1))
    
    return a * pow(a, b-1)

def fact(a):
    
    if a == 1:
        return 1
    
    return a * fact(a-1)
    

def search(n, A, key):

    # jika ketemu
    if A[n-1] == key:
        return 1
    
    # jika tidak ketemu
    if n < 0:
        return -1

    # rekursif
    return search(n-1, A, key)


def prima(number, i = 2):

    if (number <= 2):
        if number == 2:
            return True
        else:
            return False
    
    if (number % i == 0):
        return False
    
    if (i * i > number):
        return True
    
    return prima(number, i+1)

print(search(5, [12,3,13,4,30], 4))
print(prima(28))