Can you design an application to control the movements of the next rover to go up to Mars.
You have been told that the surface area on mars is 100m x 100m where they have
numbered the areas 1 through to 100 (please see diagram 1). The rover starts facing
south and can turn in the directions of left and right moving in metres taking a maximum of 5
commands at any time. The rover starts in number 1 and after each set of commands
reports back its current position and direction it is facing.
e.g
1. 50m
2. Left
3. 23m
4. Left
5. 4m


The above set of commands would cause the rover to report back position 4624 north.
The next set of commands would then continue from this square. Please note that the rover
cannot go out of this area so will halt all commands when it has reached its perimeter.

Diagram1....

|1   |   2 |   3 |...
---|---|---|---
|101 | 102 | 103 |...
|201 | 202 | 203 |...
|... | ... |  ...| ...
