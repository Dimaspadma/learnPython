def parsing(str_input):

    list_input = list(str_input)

    # print(list_input)

    huruf = {"A":False, "B":False, "C":False, "D":False, "F":False}
    
    # Mencari not
    for i in range(0, len(list_input)):
        if list_input[i] == "!":
            # print("test")
            huruf[list_input[i+1]] = not huruf[list_input[i+1]]
            list_input[i] = ""
        
    list_input.remove("")

    print(list_input)
        
    for i in range(0, len(list_input)):
        if list_input[i] == "+":
            print(huruf[list_input[i-1]] or huruf[list_input[i+1]])
        
    
    # print(huruf)
