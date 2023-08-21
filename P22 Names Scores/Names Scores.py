import string

names_path = "p022_names.txt"

def importNamesFromTxt(path):
    with open(path, "r") as txt:
        content = txt.read()
        content_list = content.replace("\"", "").split(",")
        print(content_list)
    return content_list

def StrToIntArrBasedOnAlphabet(input_string):
    integers = list()
    for x in input_string:
        integers.append(string.ascii_uppercase.index(x)+1)
    return integers

def namesScores(names_list):
    sum_of_scores = 0
    names_list = sorted(names_list)
    for name in names_list:
        score = sum(StrToIntArrBasedOnAlphabet(name))*(names_list.index(name)+1)
        sum_of_scores += score
    return sum_of_scores

names = importNamesFromTxt(names_path)
final_score = namesScores(names)
print(final_score)