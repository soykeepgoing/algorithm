def solution(routes):
    answer = 0
    new_routes = [sorted(route) for route in routes]
    new_routes.sort(key = lambda x: (x[1]))
    point = -30001
    for route in new_routes:
        if point < route[0]:
            point = route[1]
            answer += 1
    return answer
