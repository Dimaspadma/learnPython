def kubus(x):
    return x * x * x


kubusLambda = lambda x : x*x*x

print("Normal function: ", kubus(5))
print("Lambda function: ", kubusLambda(5))


# ====
def test(other_func, umur):

    nama = other_func(umur)

    print(nama)

def gabung(umur):
    return f"Umurku {umur} tahun"

test(gabung, 18)