def solve(wins, draws, scored, canced):
    size = len(wins)
    first_index = []
    second_index = []
    first = -1
    second = -1

    result = [-1,-1]

    for i in range (size):
        term_score = (wins[i]*size) + draws[i]
        if term_score > first:
            second = first
            second_index = first_index
            first = term_score
            first_index = [i]
        elif term_score == first:
            first_index.append(i)
        elif term_score == second:
            second_index.append(i)
    
    if (len(first_index) == 1):
        result[0] = first_index[0]
        if (len(second_index) == 1):
            result[1] = second_index[0]
        else:
            first = -5000
            first_index2 = 0
            for j in second_index:
                term_score = scored[j] - canced[j]
                if term_score > first:
                    first = term_score
                    first_index2 = j
            result[1] = first_index2
    else:
        first = -5000
        second = -5000
        first_index2 = 0
        second_index2 = 0
        for j in first_index:
            term_score = scored[j] - canced[j]
            if term_score > first:
                second = first
                second_index2 = first_index2
                first = term_score
                first_index2 = j
        result[0] = first_index2
        result[1] = second_index2

    return result

wins= [3,2,4]
draws=[5,1,2]
scored=[30,32,40]
canced=[32,40,50]

print(solve(wins,draws, scored,canced))