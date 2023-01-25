import unittest
from . import rover

class test_rover(unittest.TestCase):
    def test_one(self):
        r = rover.Rover()
        r.move_east_west(10)
        self.assertEqual(r.longitude, 11)
        
    def test_two(self):
        r = rover.Rover()
        r.rotate("right")
        r.rotate("right")
        self.assertEqual(r.orientation,1)

    def test_three(self):
        r = rover.Rover()
        r.rotate("left")
        self.assertEqual(r.orientation,2)

    def test_four(self):
        r = rover.Rover()
        r.move_north_south(50)   
        r.rotate("left")
        r.move_east_west(23)
        r.rotate("left")
        r.move_north_south(4)
        self.assertEqual(r.longitude, 24)
        self.assertEqual(r.latitude, 46) 
        self.assertEqual(r.orientation, 1)

    def test_five(self):
        r = rover.Rover()
        r.move_north_south(100)
        self.assertEqual(r.longitude,1)
        self.assertEqual(r.latitude, 99)
        self.assertEqual(r.orientation,3)