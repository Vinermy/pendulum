from cmath import sqrt, pi
from numpy import linspace

class SimplePendulumSimulation():
    length: float  # Length of the string in meters
    theta0: float  # Starting angle in radians (counterclockwise from the srtaight down position)
    theta: float   # Current angle in radians (counterclockwise from the straight down position)
    g: float  # Acceleration due to gravity in meters per second per second
    accelertion: float  # Tangential acceleration in meters persecond per second

    def __init__(self, _length: float, _theta: float, _g=9.81):
        self.length = _length
        self.theta0 = _theta
        self.theta = _theta
        self.g = _g

    def precalculate_positions(self, precision: float) -> None:
        pass