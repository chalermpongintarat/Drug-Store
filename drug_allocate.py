with open("drug_list.txt", "r") as file: 
    lines = file.read().split("\n")
    
    find_1 = "(" # () {} [] ' , - _
    find_2 = "{"
    find_3 = "["
    find_4 = "'"
    find_5 = ","
    find_6 = "-"
    find_7 = "_"

    with_symbol = []
    without_symbol = []

    with_symbol_line = ""
    without_symbol_line = ""

    for line in lines:
        if find_1 in line or find_2 in line or find_3 in line or find_4 in line or find_5 in line or find_6 in line or find_7 in line:
            with_symbol.append(line)
        else:
            without_symbol.append(line)

    f = open("drug_with_symbol.txt", "w")
    for line in with_symbol:
        f.write(str(line))
        f.write("\n")
    f.close()

    f = open("drug_without_symbol.txt", "w")
    for line in without_symbol:
        f.write(str(line))
        f.write("\n")
    f.close()
