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