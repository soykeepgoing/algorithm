import sys 
input = sys.stdin.readline 

def get_area(orders): 
    direction = [[0, 1], [1, 0], [0, -1], [-1, 0]]
    direction_idx = 0 
    points = [[0, 0]] 
    point_now = [0, 0]
    for order in orders:
        if order == 'L':
            direction_idx = (direction_idx - 1) % 4 
        elif order == 'R':
            direction_idx = (direction_idx + 1) % 4
        elif order in ('F', 'B'):
            dx, dy = direction[direction_idx]
            if order == 'B':
                dx, dy = -dx, -dy
            x = point_now[0] + dx
            y = point_now[1] + dy
            points.append([x, y])
            point_now = [x, y]

    x_coords, y_coords = zip(*points)
    x_min, x_max = min(x_coords), max(x_coords)
    y_min, y_max = min(y_coords), max(y_coords)
    area = (x_max - x_min) * (y_max - y_min)
    return area

if __name__ == '__main__':
    N = int(input())
    areas = [] 
    for _ in range(N):
        orders = input()
        areas.append(get_area(orders))
    
    for i in range(N):
        print(areas[i])
