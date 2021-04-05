"""
Name  : Maskumambang Padmanegara
NIM   : A11.2020.12496
Group : A11.4204
"""

from functions import *

# Main entry point
def main():

  B = [15, 12, 20, 50, 100]

  # Display main
  print("""== Mengubah nilai List ==
- 0 untuk exit
  """)
  
  # Bubble Sort
  bubbleSort(B, ascOrDesc(B))

  # main loop
  while True:

    print("* List : {}".format( B ))

    # Input user
    index_selected = int(input("> Pilih element : "))

    # Break program
    if index_selected > len(B) or index_selected <= 0:
      break

    change_element = int(input("> Ubah nilai  : "))

    # Change element
    B[index_selected-1] = change_element

    # Jika array belum urut maka diurutkan
    if not isSorted(B, ascOrDesc(B)):
      # Bubble Sort
      bubbleSort(B, ascOrDesc(B))

  # When exit
  print("\n=> Your List : {}\ndone ;)".format(B))


# Run main
if __name__ == "__main__":
  main()