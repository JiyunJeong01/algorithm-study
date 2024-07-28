def solution(n):
    answer = []
    
    def hanoi(a,b,c,n):
        if n==1:
            answer.append([a,b]) 
        else:
            hanoi(a,c,b,n-1) 
            hanoi(a,b,c,1)
            hanoi(c,b,a,n-1)
            
    hanoi(1,3,2,n)
    
    return answer