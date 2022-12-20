""""
Mars Rover simulator
An application to control the movements of the next rover to go up to Mars.
The surface area on mars is 100m x 100m where they have
numbered the areas 1 through to 100 like this:
------------------------
|   1 |   2 |   3 | ... |
| 101 | 102 | 103 | ... |
| 201 | 202 | 203 | ... |
| 301 | 302 | 303 | ... |
| ... | ... | ... | ... |

The rover starts facing south and can turn in the directions of left and right 
moving in metres taking a maximum of 5 commands at any time. 
The rover starts in number 1 and after each set of commands reports back its 
current position and direction it is facing.
e.g
1. 50m
2. Left
3. 23m
4. Left
5. 4m
The above set of commands would cause the rover to report back position 4624 north.
"""

from enum import Enum

class Rover():

    class compass(Enum):
        North = 1
        East = 2
        South = 3
        West = 4

    def __init__(self):
        # Entry point for program.  Create a Rover object
        self.latitude = 0
        self.longitude = 1
        self.orientation = 3
        self.rover_commands()

    def rotate(self,direction):
        if direction == "LEFT":
            self.orientation -= 1
        else:
            self.orientation += 1
        if self.orientation == 0:
            self.orientation = 4
        if self.orientation == 5:
            self.orientation = 1

    def move(self,distance):
        hit_boundary = False
        if (self.orientation == 1 or self.orientation == 3):
            hit_boundary = self.move_north_south(distance)
        else:
            hit_boundary = self.move_east_west(distance)
        return hit_boundary

    def move_north_south(self,distance):
        new_position = 0
        hit_boundary = False
        if self.orientation == 1:
            distance = 0 - distance
        new_position = self.latitude + distance
        if new_position < 0:
            new_position = 0
            hit_boundary = True
        if new_position > 99:
            new_position = 99
            hit_boundary = True
        self.latitude = new_position
        return hit_boundary

    def move_east_west(self,distance):
        new_position = 0
        hit_boundary = False
        if self.orientation == 4:
            distance = 0 - distance
        new_position = self.longitude + distance
        if new_position < 1:
            new_position = 1
            hit_boundary = True
        if new_position > 100:
            new_position = 100
            hit_boundary = True
        self.longitude = new_position
        return hit_boundary

    def print_rover(self):
        print("Current position: ", 
        str(self.latitude * 100 + self.longitude).rjust(4,'0'), 
        self.compass(self.orientation).name) 

    def validate_commands(self,commands):
        """    
        Takes an array of commands entered by the user and validates the content
        There must be five or fewer commands and the commands are either "left",
        "right" or an integer value followed by an "m"
        If any invalid commands are found, return an empty array and allow the 
        user to enter another set 
        """
        valid_commands = []
        if len(commands) > 5:
            print("Cannot enter more than five commands")
            return []
        for cmd in commands:
            if cmd.upper() == "LEFT" or cmd.upper() == "RIGHT":
                valid_commands.append(cmd)
            elif (cmd[len(cmd) - 1]).upper() == "M":
                try:
                    valid_commands.append(int(cmd[:len(cmd)-1]))
                except ValueError:
                    print("Invalid command entered ", cmd)
                    return []
            else:
                print("Invalid command entered - ", cmd)
                return []      
        return valid_commands

    def rover_commands(self):
        commands = []
        command_string = ""
        valid_commands = []
        hit_boundary = False
        self.print_rover()
        
        # Prompt for commands.  Exit if no commands are entered
        while True:
            command_string = input("Enter Rover commands:")
            commands = command_string.split(',')
            if len(commands) == 1 and commands[0] == '':
                print("Rover halted")
                return
            valid_commands = self.validate_commands(commands)
            # valid_commands is an array of mixed types, set by validate_commands
            # Any 'int' commands must be movements, and anything else is a rotation
            for cmd in valid_commands:
                if type(cmd) == int:
                    hit_boundary = self.move(cmd)    
                else:
                    self.rotate(cmd.upper())
                if hit_boundary == True:
                    print("Boundary hit.  Rover has halted")
                    break

            self.print_rover()

r = Rover()


    