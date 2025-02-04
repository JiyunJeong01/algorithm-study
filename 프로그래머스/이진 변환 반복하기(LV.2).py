def solution(s):
    count = 0
    deleteZero = 0
    while (s!= '1'):
        count +=1
        deleteZero += s.count('0')
        
        s = s.replace('0','')
        length = len(s)
        s = format(length, 'b')
        
        #내장함수인 format을 쓰지 않고 2진변환 하는 방법
        """
        new_s = []
        while (length > 0):
            new_s.append(str(length % 2))
            length = length // 2
        s = ''.join(reversed(new_s))
        """

    
    answer = [count, deleteZero]
    return answer