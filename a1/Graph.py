import Point as pt
import Street as st
import Edge as eg

intersection_dict = {}

class Graph(object):
    # __slots__ = ('Street_dict', 'GraphEdge_dict', 'GraphPoint_dict', 'V')
    V = 0
    Street_dict = {}
    GraphEdge_dict = {}
    GraphPoint_dict = {}

    def is_Parallel(self, edge1, edge2):

        x1, y1 = edge1.src[0], edge1.src[1]
        x2, y2 = edge1.dst[0], edge1.dst[1]
        x3, y3 = edge2.src[0], edge2.src[1]
        x4, y4 = edge2.dst[0], edge2.dst[1]

        if  x4 - x3 == 0 or x2 - x1 == 0:
            return False

        ratio_y = (y4 - y3) / (x4 - x3)
        ratio_x = (y2 - y1) / (x2 - x1)

        if ratio_x == ratio_y:
            return True
        else:
            return False

    def intersect(self, edge1, edge2):
        x1, y1 = edge1.src[0], edge1.src[1]
        x2, y2 = edge1.dst[0], edge1.dst[1]
        x3, y3 = edge2.src[0], edge2.src[1]
        x4, y4 = edge2.dst[0], edge2.dst[1]

        # xnum = ((x1 * y2 - y1 * x2) * (x3 - x4) - (x1 - x2) * (x3 * y4 - y3 * x4))
        # xden = ((x1 - x2) * (y3 - y4) - (y1 - y2) * (x3 - x4))
        # if xden == 0:
        #     return False
        # xcoor = xnum / xden
        # print(xcoor)
        #
        # ynum = (x1 * y2 - y1 * x2) * (y3 - y4) - (y1 - y2) * (x3 * y4 - y3 * x4)
        # yden = (x1 - x2) * (y3 - y4) - (y1 - y2) * (x3 - x4)
        # if yden == 0:
        #     return False
        # ycoor = ynum / yden
        # intersect = (xcoor, ycoor)
        # print(tuple(intersect))
        # return tuple(intersect)

        xnum = ((x1 - x3) * (y3 - y4) - (y1 - y3) * (x3 - x4))
        xden = ((x1 - x2) * (y3 - y4) - (y1 - y2) * (x3 - x4))
        if xden == 0:
            return False
        t = xnum / xden

        ynum = ((x1 - x2) * (y1 - y3) - (y1 - y2) * (x1 - x3))
        yden = (x1 - x2) * (y3 - y4) - (y1 - y2) * (x3 - x4)
        if yden == 0:
            return False
        u = - ynum / yden

        xcoor = float(x1 + t * (x2 - x1))
        ycoor = float(y1 + t * (y2 - y1))
        if (t >= 0 and t <= 1 and u >= 0 and u <= 1):
            intersect = (xcoor, ycoor)
            return tuple(intersect)
        else:
            return False

        # if xcoor >= 0 and xcoor <= 1 and ycoor >= 0 and ycoor <= 1:
        #     return tuple(xcoor, ycoor)
        # else:
        #     return False
    #
    # def get_intersection_dict(self):
    #     print(intersection_dict)
    #     return intersection_dict


    def add_street(self, street_name, coordinate_tuple):
        if street_name in self.Street_dict:
            print("Error: this street already exists!")
            return False
        temp = st.Street(street_name, coordinate_tuple)

        if len(self.Street_dict) == 0:
            self.Street_dict[street_name] = temp
            return self.Street_dict[street_name]

        temp_intersection = []
        for street in self.Street_dict.values():
            result = self.check_intersection(temp, street)
            for i in result:
                if i in temp_intersection:
                    continue
                else:
                    temp_intersection.append(i)
            # temp_intersection = temp_intersection + self.check_intersection(temp, street)

        for intersection in temp_intersection:
            if not intersection in intersection_dict:
                intersection_dict[intersection] = 2
            else:
                intersection_dict[intersection] += 1
        self.Street_dict[street_name] = temp
        return self.Street_dict[street_name]

    def check_intersection(self, temp, street):
        temp_edge = temp.Edge_list
        street_edge = street.Edge_list

        intersection_list = []

        for i in temp_edge:
            for j in street_edge:

                if self.is_Parallel(i, j):
                    continue
                else:
                    result = self.intersect(i, j)
                    if result == False:
                        continue
                    else:
                        intersection_list.append(result)
                        i.add_intersection(result)
                        j.add_intersection(result)
        # print("check intersection list")
        # print(intersection_list)
        return intersection_list


    def add_graph(self, p1, p2):
        if p1[0] == p2[0] and p1[1] == p2[1]:
            return False
        src, dst = p1, p2
        if not src in self.GraphPoint_dict:
            self.V += 1
            self.GraphPoint_dict[src] = self.V
        if not dst in self.GraphPoint_dict:
            self.V += 1
            self.GraphPoint_dict[dst] = self.V
        self.GraphEdge_dict[(src, dst)] = (self.GraphPoint_dict[src], self.GraphPoint_dict[dst])

    def rm_street(self, street_name):
        if not street_name in self.Street_dict:
            print("Error: this street does not exist!")
            return False
        street = self.Street_dict[street_name]
        temp_intersection = []

        for edge in street.Edge_list:
            edge.notexist_intersection()
            if len(edge.intersection_list) > 0:
                for intersection in edge.intersection_list:
                    temp_intersection.append(intersection)
                    # print("temp intersection:")
                    # print(temp_intersection)
        for intersection in temp_intersection:
            # print("intersection_dict:")
            # print(intersection_dict)
            intersection_dict[intersection] -= 1
            if intersection_dict[intersection] <= 1:
                intersection_dict.pop(intersection)
                # for intersection in temp_intersection:
                #     intersection_dict[intersection] -= 1
                #     if intersection_dict[intersection] <= 1:
                #         intersection_dict.pop(intersection)
        self.Street_dict.pop(street_name)
        return True

    def mod_street(self, street_name, coorindate_tuple):
        if not street_name in self.Street_dict:
            print("Error: this street does not exist!")
            return False
        self.rm_street(street_name)
        self.add_street(street_name, coorindate_tuple)

    def generate_graph(self):
        for street in self.Street_dict.values():
            for edge in street.Edge_list:
                if len(edge.intersection_list) > 0:
                    if len(edge.notexist_intersection()) == 0:
                        continue
                    temp = edge.re_intersection()
                    self.add_graph(edge.src, temp[0])
                    for i in range(len(temp) - 1):
                        self.add_graph(temp[i], temp[i + 1])
                    self.add_graph(temp[-1], edge.dst)

    def print_graph(self):
        self.GraphPoint_dict = {}
        self.GraphEdge_dict = {}
        self.V = 0
        self.generate_graph()
        GraphPointList = list(self.GraphPoint_dict.items())

        print("V = {")
        for i in GraphPointList:
            print("\t%d: (%s, %s)" % (i[1], round(i[0][0], 3), round(i[0][1], 3)))
        print("}")

        print("E = {")
        for edge in self.GraphEdge_dict.values():
            print("\t<%s,%s>," % (str(edge[0]), str(edge[1])))
        print("}")
