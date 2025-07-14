def get_team_and_time(team, time):
    team_win = int(team) // 2
    team_lose = team_win ^ 1
    timeM, timeS = int(time.split(':')[0]), int(time.split(':')[1])
    time = timeM * 60 + timeS 
    return team_win, team_lose, time

if __name__ == '__main__':
    N = int(input())
    results = [] 
    for _ in range(N):
        team, time = list(input().split())
        results.append([team, time])

    score = [0, 0] 
    times_now = [48 * 60, 48 * 60]
    times_cum = [0, 0]
    for team, time in results: 
        team_win, team_lose, time = get_team_and_time(team, time)
        score[team_win] +=1
        if score[team_win] > score[team_lose]: 
            if times_now[team_win] == 48 * 60:
                times_now[team_win] = time 
        elif score[team_win] == score[team_lose]:
            times_cum[team_lose] += time - times_now[team_lose]
            times_now[team_lose] = 48 * 60
    
    times_final = []
    for i in range(2):
        time = 0 
        time += times_cum[i]
        time += 48 * 60 - (times_now[i])
        M = time // 60 
        S = time % 60
        print("{0:02d}:{1:02d}".format(M, S))

