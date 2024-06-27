def solution(record):
    answer = []
    id_dic = {}
    for i in record:
        s = i.split()
        if (s[0] == "Enter"):
            id_dic[s[1]] = s[2]
        elif (s[0] == "Change"):
            id_dic[s[1]] = s[2]

    for i in record:
        s = i.split()
        if (s[0] == "Enter"):
            answer.append(id_dic[s[1]] + "님이 들어왔습니다.")
        elif (s[0] == "Leave"):
            answer.append(id_dic[s[1]] + "님이 나갔습니다.")

    return answer