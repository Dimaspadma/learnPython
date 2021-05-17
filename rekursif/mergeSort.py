# Fungsi untuk membagi sampai array terkecil
def merge_sort(arr):

    # list harus memiliki elemen
    if len(arr) > 1:
        
        # Mencari titik tengah list
        mid = len(arr) // 2

        # membagi list menjadi dua bagian
        # kiri
        L = arr[:mid]

        # dan kanan
        R = arr[mid:]

        # mengulangi pembagian list sampai menjadi terkecil
        merge_sort(L)
        merge_sort(R)

        # menggabungkan kembali
        merge(arr, L, R)

# fungsi untuk menggabungkan kembali list yang terpecah
def merge(arr, L, R):

    # index mulai dari 0
    i = j = k = 0

    # jika kedua list, list L dan R memiliki element
    while i < len(L) and j < len(R):
        if L[i] < R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        
        k += 1
    
    # Sisa dari while di atas
    while i < len(L):
        arr[k] = L[i]
        i += 1
        k += 1
    
    while j < len(L):
        arr[k] = R[j]
        j += 1
        k += 1
        


    


L = [5,3,2, 1, 8]
merge_sort(L)
print("final", L)
print("test", merge_sort(L))