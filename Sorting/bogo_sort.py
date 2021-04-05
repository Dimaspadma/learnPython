# Bogo Sort
# cara kerjanya melempar kartu ke udara,
# jika belum urut maka dilempar lagi, terus menerus sampai urut.
# Kemungkinannya O(?)


# membandingkan element n dengan n-1
def isSorted(list_data):

# def bogoSort(list_data):
#   while not isSorted(list_data):

import random

def main():
  L = [1,3,4,5]
  random.shuffle(L)
  print(L)

if __name__ == "__main__":
  main()