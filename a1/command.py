import re
import Point

'''
    Parse input Command: input, error should be output to standard error
    return a dictionary
    :param parse_dict a dict which contains command, street name and GPS coordinate tuple list
    :param input_command
    :param coordinate_list a list  which contains original coordinates
    :param new_coordinate_list a list which contains coordinates in specific format
'''

class command(object):
    '''
        Split the input command into three strings, and save them in parse_dict separately
        Here contains several conditions that the programme will return Error:
            1. 'add' only have src GPS coordinate and is lack of dst GPS coordinate
            2. When the input command is Null
            3.
    '''




    def command_input(inputStr):
        command = re.compile(r'^(add|mod|rm|gg)(.*)$')
        # street = re.compile(r'^\s*\"(.+)\"\s*((\s*\(\s*-?(\s*\d+)+\s*\,\s*-?(\s*\d+)+\s*\)){1,})\s*$')
        # street = re.compile(r'^\s\"([A-Za-z]+\s*[A-Za-z]*)\"\s((\s*\(\s*-?(\d+)+\s*\,\s*-?(\d+)+\s*\)){1,})$')
        # street = re.compile(r'^\s\"([A-Za-z]+\s*[A-Za-z]*\s*[A-Za-z]*\s*)\"\s((\s*\(-?(\d+)+\,-?(\d+)+\)){1,})\s*$')
        street = re.compile(r'^\s\"([A-Za-z]+\s*[A-Za-z]*\s*[A-Za-z]*\s*)\"\s*((\s\(-?(\d+)+\,-?(\d+)+\)){1,})$')
        rm = re.compile(r'^\s*\"(.+)\"\s*$')
        gg = re.compile(r'^\s*$')
        coordinate = re.compile(r'\((-?\d+)\,(-?\d+)\)')

        parse_dict = {}
        input_command = re.match(command, inputStr)
        if input_command == None:
            print("Error0: incorrect input!")
            return False

        parse_dict['command'] = input_command.group(1)
        # print(parse_dict)
        input_street = input_command.group(2).lower()
        # print(input_street)
        if parse_dict['command'] == 'add' or parse_dict['command'] == 'mod':

            input_command = re.match(street, input_street)

            if input_command == None:
                print("Error: incorrect input!")
                return False
            parse_dict['street_name'] = input_command.group(1).lower()
            # print(parse_dict)

            coordinate_list = re.findall(coordinate, input_command.group(2).lower())
            if len(coordinate_list) < 2:
                print("Error: incorrect input!")
                return False
            new_coordinate_list = []
            for i in range(len(coordinate_list)):
                # new_coordinate = Point(coordinate_list[i][0], coordinate_list[i][1])
                new_coordinate = (float(coordinate_list[i][0]), float(coordinate_list[i][1]))
                new_coordinate_list.append(new_coordinate)
            parse_dict['GPS_coordinate'] = new_coordinate_list
            # print(parse_dict)

        elif parse_dict['command'] == 'rm':
            input_command = re.match(rm, input_street)
            if input_command == None:
                print("Error: incorrect input!")
                return False
            parse_dict['street_name'] = input_command.group(1)

        elif parse_dict['command'] == 'gg':
            input_command = re.match(gg, input_street)
            if input_command == None:
                print("Error: incorrect input!")
                return False
        else:
            print("Error: incorrect input!")
            return False
        return parse_dict
