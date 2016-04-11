import math
import random


def create_random_points(n):
    rand = random.seed()
    random_points = [(rand.randint(0, 100), rand.randint(0, 100))]
    return random_points


def create_random_marked_points(n, marks=[]):
    rand_mp = random.seed()
    rand_pts = []
    if marks is None:
        for i in range(n):
            rand_pts.append(rand_mp.randint(0, 100), rand_mp.randint(0,100), rand_mp.choice(marks))
    else:
        for i in range(n):
            rand_pts.append(rand_mp.randint(0, 100), rand_mp.randint(0,100), rand_mp.choice(marks))
    return rand_pts


def euclidean_distance(a, b):
    distance = math.sqrt((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2)
    return distance


def manhattan_distance(a, b):
    distance = abs(a[0] - b[0]) + abs(a[1] - b[1])
    return distance


def check_in(points, point_list):
    return points in point_list


def getx(points):
    return points[0]


def gety(points):
    return points[1]
