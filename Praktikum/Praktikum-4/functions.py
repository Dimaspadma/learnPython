"""
Name  : Maskumambang Padmanegara
NIM   : A11.2020.12496
Group : A11.4204
"""

# Bubble Sort
def bubbleSort(List, keterangan="asc"):

  # Jika masih bisa di swap maka lanjut while
  swaper = True

  while swaper:

    # set swaper to False agar bisa keluar dari perulangan
    swaper = False

    # get index
    for index in range(len(List) - 1):

      # Jika element n < n+1 maka tukar dan swap true agar tetap lanjut
      # Ascending
      if List[index] > List[index + 1] and keterangan == "asc":
        (List[index], List[index + 1]) = (List[index + 1], List[index])
        swaper = True

      # Descending
      if List[index] < List[index + 1] and keterangan == "desc":
        (List[index], List[index + 1]) = (List[index + 1], List[index])
        swaper = True

  return List


# Memilih ascending atau descending
def ascOrDesc(List):
  # jika element pertama < elemen terakhir maka ascending
  if List[0] <= List[-1]:
    return "asc"

  # jika element pertama > elemen terakhir maka descending
  elif List[0] > List[-1]:
    return "desc"


# Mengecek apakah list sudah urut atau belum
def isSorted(List, keterangan="asc"):
  # jika ascending, cek apakah index n < n-1
  if keterangan == "asc":
    for index in range(1, len(List)):
      # jika n < n-1 terpenuhi maka berarti tidak urut
      if List[index] < List[index - 1]:
        return False

  # jika descending, cek apakah index panjang_list-n > panjang_list - n - 1; hitung mundur
  elif keterangan == "desc":
    for index in range(len(List)-1, 0, -1):
      if List[index] > List[index - 1]:
        return False

  # jika urut maka mengembalikan nilai True
  return True