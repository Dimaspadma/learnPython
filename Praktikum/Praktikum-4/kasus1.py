L = ["katak", "burung", "ayam", "ibu", "dia"]

input_user = int(input("Karakter huruf : "))

for i in range(len(L)):
    if input_user == len(L[i]):
        print(L[i], end=" ")