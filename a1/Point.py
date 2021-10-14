'''
    Point: GPS coordinate, contains start position and end position
'''


class Point(object):
    def __init__(self, x, y):
        self.x = float(x);
        self.y = float(y);

    def __repr__(self):
        return '({0: .2f}, {1: .2f})'.format(self.x, self.y)

    def __str__(self):
        return repr(self)
