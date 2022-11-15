#= Mars Rover simulator
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
=#
using Printf

compass = ["North", "East", "South", "West"]

mutable struct Rover
    # Object to represent the position of the rover
    latitude::Int
    longitude::Int
    orientation::Int

    function Rover()
        # Constructor for the rover object
        new(0,1,3)   #= Always start in first square facing south =#
    end
end

function Base.show(io::IO, rover::Rover)
    # Add new method to Base.show to print representation of the position of the rover
    @printf(io, "Current position: %d - %s" , rover.latitude * 100 + rover.longitude, compass[rover.orientation])
end

function rotate!(rover::Rover, direction)
    # Represent "north" as 1, "east as 2 etc
    if(direction == "LEFT")
        # counter-clockwise turn
        rover.orientation -= 1
    else
        # clockwise turn
        rover.orientation += 1
    end
    # check for "overflow"
    if(rover.orientation == 0)
        rover.orientation = 4
    end
    if(rover.orientation == 5)
        rover.orientation = 1
    end
end

function move!(rover::Rover, distance)  
    hit_boundary = false
    if(rover.orientation == 1 || rover.orientation == 3)
        hit_boundary = move_north_south!(rover, distance)
    else
        hit_boundary = move_east_west!(rover, distance)
    end
    return hit_boundary
end

function move_north_south!(rover::Rover, distance)
    new_position = 0
    hit_boundary = false
    if rover.orientation == 1
        distance = 0 - distance
    end
    new_position = rover.latitude + distance
    # Check for bounday hit
    # Set sensible location
    if new_position < 0
        new_position = 0
        hit_boundary = true
    end
    if new_position > 99
        new_position = 99
        hit_boundary = true
    end
    rover.latitude = new_position
    return hit_boundary
end

function move_east_west!(rover::Rover, distance)
    new_position = 0
    hit_boundary = false
    if rover.orientation == 4
        distance = 0 - distance
    end
    new_position = rover.longitude + distance
    # Check for bounday hit
    # Set sensible location
    if new_position < 1
        new_position = 1
        hit_boundary = true
    end
    if new_position > 100
        new_position = 100
        hit_boundary =true
    end
    rover.longitude = new_position
    return hit_boundary
end

function start_rover()
    # Entry point for program.  Create a Rover object
    rover = Rover()

    commands = []
    command_string = ""
    valid_commands = []
    hit_boundary = false

    println(rover)
    
    # Now prompt for commands.  Exit if no commands are entered
    while true
        print("Enter Rover commands:")
        command_string = readline()
        commands = split(command_string)
        if length(commands) == 0
            println("Rover halted")
            return
        end
        valid_commands = validate_commands(commands)
        #= valid_commands is an array of mixed types, set by validate_commands
           Any Int64 commands must be movements, and anything else is a rotation
        =#
        for cmd ∈ valid_commands
            if typeof(cmd) == Int64
                hit_boundary = move!(rover,cmd)    
            else
                rotate!(rover, uppercase(cmd))
            end
            if hit_boundary == true
                println("Boundary hit.  Rover has halted")
                break
            end
        end
        # Display rover location 
        println(rover)
    end
end

function validate_commands(commands)
    #= Takes an array of commands entered by the user and validates the content
       There must be five or fewer commands and the commands are either "left",
       "right" or an integer value followed by an "m"
       If any invalid commands are found, return an empty array and allow the 
       user to enter another set 
    =# 
    valid_commands = []
    if length(commands) > 5
        println("Cannot enter more than five commands")
        return []
    end
    for cmd ∈ commands
        if uppercase(cmd) == "LEFT" || uppercase(cmd) == "RIGHT"
            push!(valid_commands, cmd)
        elseif uppercase(SubString(cmd, length(cmd))) == "M"
            try
                push!(valid_commands,parse(Int,SubString(cmd, 1, length(cmd)-1)))
            catch
                println("Invalid command entered ", cmd)
                return []
            end
        else
            println("Invalid command entered - ", cmd)
            return []
        end
    end
    return valid_commands
end

# Start the simulation
start_rover()