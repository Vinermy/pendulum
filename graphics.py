from PIL import Image
from PIL import ImageDraw


class SimplePendulumRenderer:
    def __init__(self, frame_size: tuple[int, int] = (400, 400), length: float = 1):
        self.frame_size = frame_size
        self.length = length

    def frame_space_interpolate(self, xy: tuple[float, float]) -> tuple[int, int]:
        """
        Simulation space has point (0; 0) at the pendulum's fulcrum.
        Frame space has the point (0; 0) in the top-left corner,
        the pendulum is centered, and height is equal to 2.5 times
        the length of the pendulum.
        This function interpolates the point from simulation space
        to frame space, while maintaining the aspect ratio
        :param xy: Point in the simulation space
        :return: Point in the frame space
        """

        multiplier = self.frame_size[1] / (self.length * 2.5)
        x_translation = self.frame_size[0] / 2
        y_translation = (self.frame_size[1] - 1.75 * self.length * multiplier)
        return (
            int(xy[0] * multiplier + x_translation),
            int(xy[1] * multiplier + y_translation)
        )

    def draw_frame(self, pos: tuple[float, float]) -> Image.Image:
        frame = Image.new('RGB', self.frame_size, (255, 255, 255))
        draw = ImageDraw.Draw(frame)
        draw.ellipse((self.frame_space_interpolate((-1, 1)),
                      self.frame_space_interpolate((1, -1))), fill=(255, 0, 0))

        draw.line((
            self.frame_space_interpolate((0, 0)),
            self.frame_space_interpolate(pos)
        ), fill=(0, 255, 0))

        xy1 = self.frame_space_interpolate((pos[0] - 5, pos[1] - 5))
        xy2 = self.frame_space_interpolate((pos[0] + 5, pos[1] + 5))

        draw.ellipse((
            (min(xy1[0], xy2[0]), min(xy1[1], xy2[1])),
            (max(xy1[0], xy2[0]), max(xy1[1], xy2[1]))
        ), fill=(0, 0, 255))

        return frame

    def test_interpolation(self):
        self.length = 40
        frame = Image.new('RGB', self.frame_size, (255, 255, 255))
        draw = ImageDraw.Draw(frame)
        for x in range(-50, 51):
            for y in range(-50, 51):
                draw.point(
                    self.frame_space_interpolate((x, y)),
                    fill=(0, 0, 0)
                )
        return frame
