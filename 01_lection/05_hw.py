import math

d = int(input())
Px, Py = list(map(int, input().split(' ')))

Ax, Ay = 0, 0
Bx, By = d, 0
Cx, Cy = 0, d

p1 = (Ax - Px) * (By - Ay) - (Bx - Ax) * (Ay - Py)
p2 = (Bx - Px) * (Cy - By) - (Cx - Bx) * (By - Py)
p3 = (Cx - Px) * (Ay - Cy) - (Ax - Cx) * (Cy - Py)

if (p1 >= 0 and p2 >= 0 and p3 >= 0):
    print(0)
else:
    dist_a = math.sqrt(math.pow(Px - Ax, 2) + math.pow(Py - Ay, 2))
    dist_b = math.sqrt(math.pow(Px - Bx, 2) + math.pow(Py - By, 2))
    dist_c = math.sqrt(math.pow(Px - Cx, 2) + math.pow(Py - Cy, 2))

    dist_min = min(dist_a, dist_b, dist_c)

    if dist_min == dist_a:
        print(1)
    elif dist_min == dist_b:
        print(2)
    else:
        print(3)
