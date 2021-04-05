# Algorithm for searching an item in the list. iterate an list and then compare every item with item searched.
# This search algorithm can find an item in the list unsorted;

# List
L = [2,5,3,1,7,4]

# item was we searched
find = 10

# Iterate List
for i in range(0, len(L)):

    # comparing
    if L[i] == find :
        print("We found it")

        break

# If not in list
else :
    print("nope")