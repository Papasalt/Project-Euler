triangle = [    [6],
               [4,7],
              [6,2,8],
             [9,5,4,1]]

triangle_2 = [[6],
              [4,7],
              [15,11,7,6,12,9]]

#[[6],
#[4,7],
#[6,2,8],
#[9,5,4,1]]

#[[6],
#[4,7],
#[15,11,7,6,12,9]]

#      [[6],
#      [4,7],
#[15,11,7,6,12,9]]

#      [[00],
#      [10,11],
#[20,21,22,23,24,25]]

#  [[6],
#  [4,7],
# [6,2,8],
#[9,5,4,1]]

def returnAdjacentAbove(t, e_r, e_i): #triangle, element_row, element_index
    offset = len(t[e_r])-len(t[e_r-1]) if len(t[e_r])-len(t[e_r-1]) % 2 != 0 \
        else len(t[e_r])-len(t[e_r-1])-2
    #offset indicates which element in the given row has >2 adjacent values above
    #or <2. Used on line 34.
    values = []
    if e_i < offset:
        values.append(t[e_r-1][0])
    elif e_i >= len(t[e_r])-offset:
        values.append(t[e_r-1][-1])
    else:
        2
    return values
    

def maxPathSum(t):
    new_t = t[0:len(t)-2]
    """
    new_t.append([t[2][0]+t[3][0],
                  t[2][0]+t[3][1],
                  t[2][1]+t[3][1],
                  t[2][1]+t[3][2],
                  t[2][2]+t[3][2],
                  t[2][2]+t[3][3]])
    """
    l_t = len(t)-1 # decreased len by 1 to suit 0-index
    #new_t.append([t[l_t-1][]])
    #print(t[l_t-1])
    new_row = []
    for e in range(0, len(t[len(t)-1])-1):
        """
        print(t[len(t)-2][e], "\t", len(t)-2, "\t", e)
        print(t[len(t)-1][e], "\t", len(t)-1, "\t", e)
        print(t[len(t)-1][e+1], "\t", len(t)-1, "\t", e+1)
        print("\n")
        """
        new_row.append(t[len(t)-2][e]+t[len(t)-1][e])
        new_row.append(t[len(t)-2][e]+t[len(t)-1][e+1])
        print(new_row)

def test(t):
    new_row = []
    for e in range(0, len(t[len(t)-1])-1):
        new_row.append(t[len(t)-2][e]+t[len(t)-1][e])
        new_row.append(t[len(t)-2][e]+t[len(t)-1][e+1])
    del t[-2:]
    t.append(new_row)
    """
    for e in range(0, len(t[len(t)-1])-1):
        offset = 
        
        print(t[len(t)-2][e]+t[len(t)-1][e])
        print(t[len(t)-2][e]+t[len(t)-1][e+1])
    """
print(test(triangle_2))