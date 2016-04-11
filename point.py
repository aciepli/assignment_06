import utils


def __init__(self, x, y, mark=[]):
    self.x = x
    self.y = y
    self.mark = mark


def __str__(self):
    return "[0], [1]".format(self.x, self.y)


def check_coincident(a, b):
    return a == b


def shift_point(point, x_shift, y_shift):
    x = utils.getx(point)
    y = utils.gety(point)

    x += x_shift
    y += y_shift

    return x, y
