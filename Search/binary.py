# Or Bisection Search
# is search Alghorithm where we divide in the middle of list again and again

# This algorithm must be a sorted list

L = [1, 2, 3, 4, 5, 6, 7, 8, 9]

find = 10

# key to identified a left, middle, and right list
left = 0
right = len(L) - 1

found = False

# while loop until left equal right
while left <= right and not found:

    middle = (right + left) // 2
    
    middleValue = L[middle]

    # Debug
    print("L:{}, M:{}, R:{}".format(L[left], L[middle], L[right]))


    # check if item equal to an item on middle of list
    if find == middleValue:
        print("Found it")
        found = True
        
    # if item greater than middle Value, then slide left key to middle and divide again
    elif find > middleValue:
        left = middle + 1

    # Otherwise
    elif find < middleValue:
        right = middle - 1

else:
    print("Nope")