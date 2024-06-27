num = int(input())

people_list = list(map(int,input().split()))
people_list.reverse()

stay_list = []
j = 1
snack = True

while (j != num):
    if people_list:
        if people_list[-1] == j:
            people_list.pop()
            j+=1
        else:
            if stay_list:
                if stay_list[-1] == j:
                    stay_list.pop()
                    j+=1
                else:
                    stay_list.append(people_list.pop())
            else:
                stay_list.append(people_list.pop())
    else:
        if stay_list:
            if stay_list[-1] == j:
                stay_list.pop()
                j+=1
            else:
                snack = False
                break
        else:
            snack = False
            break

if snack == True:
    print ("Nice")
else:
    print ("Sad")