'''
    Define src and dst,
    :param src: start point of lines
    :param dst: end point of lines
    :param intersection_list a list which contains intersections with this edge
'''

import Graph as G


class Edge(object):
    __slots__ = ('src', 'dst', 'intersection_list')


    def __init__(self, p1, p2):
        self.src = p1
        self.dst = p2
        self.intersection_list = []
    # return tuple(self.src, self.dst)

    # def coordinate(self):
    #     return (self.src, self.dst)
    def __repr__(self):
        # return repr(self.src) + '-->' + repr(self.dst)
        return repr(self.src) + "-->" + repr(self.dst)
    #     return "<" + repr(self.src) + ',' + repr(self.dst) + ">"

    '''
        The add_intersection function is to help us modify edge after 'add' command or 'mod' command
        The rm_intersection function is to help us modify edge after 'rm' command
        :param intersection_point is calculated by Graph().intersect function
    '''

    def add_intersection(self, intersection_point):
        if intersection_point in self.intersection_list:
            return True
        self.intersection_list.append(intersection_point)
        # print("Successfully add!")

    def rm_intersection(self, intersection_point):
        if intersection_point in self.intersection_list:
            self.intersection_list.pop(intersection_point)

    def re_intersection(self):
        if len(self.intersection_list) <= 1:
            return tuple(self.intersection_list)
        return self.intersection_list

    def notexist_intersection(self):
        notexist_intersection = []
        # print("intersection list:")
        # print(self.intersection_list)
        for intersection in self.intersection_list:
            if not (intersection in G.intersection_dict) or (G.intersection_dict[intersection] <= 1):
                notexist_intersection.append(intersection)
        # print("not exist intersection:")
        # print(notexist_intersection)

        for i in notexist_intersection:
            if i in self.intersection_list:
                self.intersection_list.remove(i)

        # for i in range(len(self.intersection_list)):
        #     if self.intersection_list[i] in notexist_intersection:
        #         self.intersection_list.pop(self.intersection_list[i])
        # print(self.intersection_list)
        return self.intersection_list
