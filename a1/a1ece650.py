#!/usr/bin/env python3
import sys
import command as cmd
import Graph as G

# YOUR CODE GOES HERE

def main():
    # YOUR MAIN CODE GOES HERE
    # sample code to read from stdin.
    # make sure to remove all spurious print statements as required
    # by the assignment


    while True:
        line = sys.stdin.readline()
        if line == "":
            break
        parse_dict = cmd.command.command_input(line)
        if parse_dict ==  False:
            continue

        # print(parse_dict)
        print("read a line:", line)

        if parse_dict['command'] == 'add':
            G.Graph().add_street(parse_dict['street_name'], parse_dict['GPS_coordinate'])
        elif parse_dict['command'] == 'rm':
            G.Graph().rm_street(parse_dict['street_name'])
        elif parse_dict['command'] == 'mod':
            G.Graph().mod_street(parse_dict['street_name'], parse_dict['GPS_coordinate'])
        elif parse_dict['command'] == 'gg':
            G.Graph().print_graph()

    print("Finished reading input")
    # return exit code 0 on successful termination
    sys.exit(0)


if __name__ == "__main__":
    main()


'''
add "weber" (1,2)(3,4) (5,6) - no space between the brackets - error
'''