path = r"C:\Users\papas\Documents\file.csv"
file = open(path,"r")
counter = 0
my_array = []
for row in file.readlines():
    print(row)
    """
    my_array[counter][0] = row[0]
    my_array[counter][1] = row[1]
    my_array[counter][2] = row[2]
    my_array[counter][3] = row[3]
    """
    counter += 1
file.close()