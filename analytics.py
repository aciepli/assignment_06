import math
import sys
import os
import point
import utils


sys.path.insert(0, os.path.abspath('..'))

from .. import point

def find_largest_city(gj):
    city = None
    max_population = 0

    for i in gj['features']:
        if i['properties']['pop_max'] > max_population:
            max_population = i['properties']['pop_max']
            city = i['properties']['name']

    return city, max_population


def mean_center(points):
    x = 0
    y = 0

    for i in points:
        x += i[0]
        y += i[1]

    x /= len(points)
    y /= len(points)

    return x, y


def average_nearest_neighbor_distance(points):

    mean_d = 0
    nearest_neighbor = math.inf

    for p in points:
        for otherPoint in points:
            if point.check_coincident(p, otherPoint):
                continue
            current_distance = utils.euclidean_distance(p, otherPoint)
            if nearest_neighbor is None:
                nearest_neighbor = current_distance
            elif nearest_neighbor > current_distance:
                nearest_neighbor = current_distance

        mean_d += nearest_neighbor
        nearest_neighbor = None

    mean_d /= len(points)

    return mean_d


def minimum_bounding_rectangle(points):

    mbr = [0, 0, 0, 0]
    x_min = 0
    x_max = 0
    y_min = 0
    y_max = 0

    for p in points:
        if p[0] < x_min:
            x_min = p[0]
        if p[0] > x_max:
            x_max = p[0]
        if p[1] < y_min:
            y_min = p[1]
        if p[1] > y_max:
            y_max = p[1]
        mbr = [x_min, y_min, x_max, y_max]

    return mbr


def mbr_area(mbr):

    l = mbr[2] - mbr[0]
    w = mbr[3] - mbr[1]
    area = l * w

    return area


def expected_distance(area, n):

    expected = 0.5 * (math.sqrt(area / n))

    return expected


def compute_critical(points):

    lower = min(points)
    upper = max(points)

    return lower, upper


def check_significant(lower, upper, observed):

    if (lower < observed) or (observed < upper):
        result = True
    else:
        result = False

    return result


def permutation(p=99, n=100):

    perm = []
    for x in range(p):
        perm.append(average_nearest_neighbor_distance(utils.create_random_points(n)))

    return perm
