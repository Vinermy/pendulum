import numpy as np
from numpy import linspace, sqrt, cos, sin

from graphics import SimplePendulumRenderer
from simple_pendulum import SimplePendulumSimulation
import matplotlib.pyplot as plt

# def lerp(value, start, end, new_start, new_end):
#     return new_start + (value - start) * ((new_end - new_start) / (end - start))

sim = SimplePendulumSimulation(
    50,
    2,
)
precision = 0.001
sim.precalculate_positions(precision)

# make data

# plot
plt.style.use('seaborn-v0_8-pastel')
fig, ax = plt.subplots()
fig.suptitle(f'L: {sim.length}м, g: {sim.g}м/с^2, T: {sim.period():.3}с,\
 dt: {sim.period() * precision:.6}с')

ax.plot(sim.time, sim.positions, linewidth=2.0)
ax.set_xlabel('Время, с')
ax.set_ylabel('Отклонение от вертикали, рад.')

# plt.show()

# phase space diagram
#
# x = [lerp(timestamp, 0, sim.period(), 0, 2 * np.pi) for timestamp in sim.time]
# y = [sim.g * sim.length * sin(pos) ** 2 + vel ** 2 / 2 for pos, vel in zip(sim.positions, sim.velocities)]
#
# fig, ax = plt.subplots(subplot_kw={'projection': 'polar'})
# ax.plot(x, y, linewidth=2.0)
# plt.show()



r = SimplePendulumRenderer(length=sim.length)

x = [r.frame_space_interpolate(pos)[0] for pos in sim.get_weight_coordinates()]
y = [r.frame_space_interpolate(pos)[1] for pos in sim.get_weight_coordinates()]
fig, ax = plt.subplots()
ax.plot(x, y, linewidth=2.0)
plt.show()

r.test_interpolation().show()
for pos in sim.get_weight_coordinates()[::1000]:
    r.draw_frame(pos).show()