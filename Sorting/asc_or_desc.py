# Memilih ascending dan descending
def ascOrDesc(List):
  # jika element pertama < elemen terakhir maka ascending
  if List[0] <= List[-1]:
    return "asc"

  # jika element pertama > elemen terakhir maka descending
  elif List[0] > List[-1]:
    return "desc"