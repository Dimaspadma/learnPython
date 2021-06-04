def getListGenap(myList):

    # ~~ from this
    # newList = []

    # for item in myList:
    #     if item % 2 == 0:
    #         newList.append(item)
    
    # return newList


    # Use list comprehension
    # ~~ to this
    return [item for item in myList if item % 2 == 0]

testList = [1,2,3,4,5,6,7,8,9,10]

# newList = getListGenap(testList)

# dipangkatkan dari bilangan ganjil
newList = lambda x, y: x+y

print("testList:", testList)
print("newList:", newList(5,2))