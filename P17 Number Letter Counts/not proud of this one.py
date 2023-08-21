place_1 = {1:"one",2:"two",3:"three",4:"four",5:"five",
                   6:"six",7:"seven",8:"eight",9:"nine"}

special = {11:"eleven", 12:"twelve"}

place_10 = {10:"ten",20:"twenty",30:"thirty",40:"forty",50:"fifty",
                60:"sixty",70:"seventy",80:"eighty",90:"ninety"}

others = {3:"hundred", 4:"thousand", 7:"million"}

places = {1:{0:"",1:"one",2:"two",3:"three",4:"four",5:"five", 6:"six",7:"seven",8:"eight",9:"nine"}, 
          2:{10:"ten",11:"eleven",12:"twelve",13:"thirteen",14:"fourteen",15:"fifteen",16:"sixteen",17:"seventeen",18:"eighteen",19:"nineteen",
             20:"twenty",30:"thirty",40:"forty",50:"fifty", 60:"sixty",70:"seventy",80:"eighty",90:"ninety"}, 
          3:"hundred", 4:"thousand"}

def constructAsWordNumeral(integer):
    word_numeral = ""
    place_values = []
    current_place_val = len(str(integer)) # 349 -> 3
    for x in str(integer): #"349"
        current_place_val -= 1
        if x != "0": place_values.append(int(x)*(10**current_place_val))
    for val in place_values:
        if val == 10 and place_values[place_values.index(val)-1] >= 100:
            if place_values[-1] < 10:
                word_numeral += " and " + places[2][10+place_values[-1]]
            else:
                word_numeral += " and " + places[2][10]
            break
        elif val == 10 and place_values[place_values.index(val)-1] < 100:
            if place_values[-1] < 10:
                word_numeral += places[2][10+place_values[-1]]
            else:
                word_numeral += places[2][10]
            break
        if val != 0:
            place = 1 + str(val).count("0") # place = 1 (digits), 2 (tens), 3 (hundred) or 4 (thousand)
        else:
            place = 1
        if place >= 3:
            if place == 3:
                word_numeral += places[1][int(str(val)[0])] + " " + places[place]
            else:
                word_numeral += places[1][int(str(val)[0])] + " " + places[place] + " "
        else:                            # ^ Gives first number in integer, e.g. 500 -> 5
            if place == 2 and place_values[0] < 100:
                word_numeral += places[place][val]
            elif place == 2 and place_values[0] >= 100:
                word_numeral += " and " + places[place][val]
            elif place == 1 and place_values[place_values.index(val)-1] >= 100:
                word_numeral += " and " + places[place][val]
            elif place == 1 and place_values[place_values.index(val)-1] < 100:
                word_numeral += places[place][val]
    #print(word_numeral)
    #print(place_values)
    return word_numeral

def numberLetterCounts(minimum, maximum):
    number_letter_count = 0
    for x in range(minimum, maximum+1):
        current_number = constructAsWordNumeral(x)
        print(current_number)
        number_letter_count += len(current_number.replace(" ", ""))
    return number_letter_count

#print(constructAsWordNumeral(10))
print(numberLetterCounts(1, 1000))