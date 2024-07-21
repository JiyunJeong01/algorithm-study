import re

# 시간 차이를 분으로 환산해서 return
def return_minute(start, end):
    start_list = list(map(int, start.split(":")))
    end_list = list(map(int, end.split(":")))
    return (((end_list[0] - start_list[0])*60) + (end_list[1] - start_list[1]))

# 시간만큼 진행된 음을 나열하고, 안에 있는지 체크 결과 return
def check(playtime, sound, m):
    # #이 붙어있는 것도 구분하기 위해 모듈 사용
    sound = re.findall(r'C#|C|D#|D|E|F#|F|G#|G|A#|A|B', sound)
    m = re.findall(r'C#|C|D#|D|E|F#|F|G#|G|A#|A|B', m)
    length = len(sound)
    play_song = []
    
    # 진행된 만큼 반복해서 총 play된 음 play_song에 저장
    for i in range (playtime):
        play_song.append(sound[i % length])
    
    # play_song 안에 존재하는지 확인
    for i in range(len(play_song) - len(m) + 1):
        if play_song[i:i + len(m)] == m:
            return True
    return False

def solution(m, musicinfos):
    term = []
    answer_time = 0
    answer = "(None)"
    for i in musicinfos:
        term = i.split(',')
        time = return_minute(term[0], term[1])
        if(check(time, term[3], m)):
            if (answer_time < time):
                answer_time = time
                answer = term[2]

    return answer