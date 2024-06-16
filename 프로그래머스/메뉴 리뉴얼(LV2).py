from itertools import combinations, permutations
from collections import Counter

suv = []
answer = []
def solution(orders, course):
    for i in course:
        suv = []
        for j in orders:
            combi = list(combinations(sorted(j), i))
            suv.extend(combi)
        counter = Counter(suv)
        
        if counter:
            max_count = max(counter.values())
            most_common = [''.join(sorted(item)) for item, count in counter.items() if count == max_count and max_count > 1]
            answer.extend(most_common)
            
    return sorted(answer)