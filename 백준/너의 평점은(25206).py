sumCredit = 0
sumScore = 0


for _ in range (20):
    lecture, credit, score = input().split()
    credit = float(credit)
    sumCredit += credit

    if (score == 'A+'):
        sumScore += (4.5 * credit)
    elif (score == "A0"):
        sumScore += (4.0 * credit)
    elif (score == "B+"):
        sumScore += (3.5 * credit)
    elif (score == "B0"):
        sumScore += (3.0 * credit)
    elif (score == "C+"):
        sumScore += (2.5 * credit)
    elif (score == "C0"):
        sumScore += (2.0 * credit)
    elif (score == "D+"):
        sumScore += (1.5 * credit)
    elif (score == "D0"):
        sumScore += (1.0 * credit)
    elif (score == "F"):
        continue
    else:
        sumCredit -=credit
        continue

print (round((sumScore / sumCredit),6))