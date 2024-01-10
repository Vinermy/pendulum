from cmath import sqrt, pi, sin, cos
from numpy import linspace


class SimplePendulumSimulation():
    length: float  # Length of the string in meters
    theta0: float  # Starting angle in radians (counterclockwise from the straight down position)
    theta: float  # Current angle in radians (counterclockwise from the straight down position)
    g: float  # Acceleration due to gravity in meters per second per second
    acceleration: float  # Tangential acceleration in meters per second per second

    def __init__(self, _length: float, _theta: float, _vel: float = 0, _g=9.81):
        self.length = _length
        self.theta0 = _theta
        self.theta = _theta
        self.velocity0 = _vel
        self.velocity = _vel
        self.positions: list[float] = [self.theta0]
        self.velocities: list[float] = [self.velocity0]
        self.time = None
        self.g = _g
        self.E = self.g * self.length * sin(self.theta0).real ** 2 + self.velocity0 ** 2 / 2

    def precalculate_positions(self, precision: float) -> None:
        time, dt = linspace(0.0, self.period(), int(self.period() / precision), retstep=True)
        self.time = time

        for _ in time:
            dv = -(self.g / self.length) * dt * sin(self.theta).real
            self.velocity += dv
            self.velocities.append(self.velocity)
            self.theta += self.velocity * dt
            self.positions.append(self.theta)

        self.positions.pop(-1)
        self.velocities.pop(-1)

    def period(self) -> float:
        return 2 * pi * sqrt(self.length / self.g).real / agm(1, cos(self.theta0 / 2).real)

    def get_weight_coordinates(self) -> list[tuple[float, float]]:
        return [(
            self.length * sin(theta/2).real * 2 * cos(theta/2).real,
            self.length * sin(theta/2).real * 2 * sin(theta/2).real
        ) for theta in self.positions]


def agm(a0: float, b0: float, tolerance: float = 1e-10) -> float:
    an = (a0 + b0) / 2
    gn = sqrt(a0 * b0).real

    while abs(an - gn) > tolerance:
        an, gn = ((an + gn) / 2), sqrt(an * gn).real

    return an
