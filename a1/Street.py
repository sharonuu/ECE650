'''
    Street class includes street name, edge list and intersection list
    :param Street name
    :param coordinate_tuple

'''

import Edge as eg

class Street(object):
    __slots__ = ('Street_name', 'Edge_list', 'intersection_list')

    # Street_name = None
    # Edge_list = None

    def __init__(self, Street_name, coordinate_tuple):
        self.Street_name = ""
        self.Edge_list = []
        self.intersection_list = []

        if len(Street_name) <= 0:
            return None
        self.Street_name = Street_name

        for i in range(len(coordinate_tuple) - 1):
            # Stay at original location
            if coordinate_tuple[i] == coordinate_tuple[i + 1]:
                continue
            else:
                # add new edge in edge class
                edge = eg.Edge(coordinate_tuple[i], coordinate_tuple[i + 1])
            self.Edge_list.append(edge)
    # def re_intersection(self):
