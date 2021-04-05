# Looping although an item we find was founded.

L = [3,6,2,1,9,14,29,12]
lengthOfList = len(L)
count = 0

# Add an item we searching into the last of list
find = 69

# store last item to temporary variable
lastItem = L[lengthOfList - 1]

# change last item to what we find
L[lengthOfList - 1] = find

# Debugging
print(L)

# while loop until reach the find item and counting
index = 0

while L[index] != find :
    count += 1
    index += 1

# Turn back list to default
L[lengthOfList - 1] = lastItem

# if count is less than length of list where is not include a last item, so (lengthOfList - 1), then we found it 
# or last item of list equal what we find
if count < lengthOfList - 1 or find == L[lengthOfList - 1]:
    print("We found it")

else:
    print("Nope")