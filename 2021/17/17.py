
t_x1 = 169
t_x2 = 206
t_y1 = -108
t_y2 = -68

def is_in_target(x,y):
    return t_x1 <= x <= t_x2 and t_y1 <= y <= t_y2

highest_y = 0
count = 0

for i in range(0,2000):
    for j in range(-500,2000):
        xv = i
        yv = j
        x,y = 0,0
        local_highest_y = 0
        while (not is_in_target(x,y)) and x<=t_x2 and y>=t_y1:
            x += xv
            if xv > 0:
                xv -= 1
            elif xv < 0:
                xv += 1
            y += yv
            yv -= 1
            if y > local_highest_y:
                local_highest_y = y
        if is_in_target(x,y):
            count += 1
            if local_highest_y > highest_y:
                highest_y = local_highest_y

print('highest:', highest_y)
print('count:', count)
            
