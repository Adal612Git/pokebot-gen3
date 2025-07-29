# Simple gait simulation with matplotlib
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


# Segment lengths (arbitrary units)
L_HIP_KNEE = 1.0
L_KNEE_ANKLE = 1.0
L_ANKLE_FOOT = 0.3

# Typical gait angles (degrees converted to radians)
# Hip: small oscillation around neutral
THETA_HIP = np.radians([10, 5, 0, -5, -10, -5, 0, 5, 10])
# Knee: flexes during swing
THETA_KNEE = np.radians([0, 10, 30, 50, 60, 50, 30, 10, 0])
# Ankle: simple movement for demonstration
THETA_ANKLE = np.radians([0, -5, -10, -5, 0, 5, 10, 5, 0])


def compute_positions(theta_hip: float, theta_knee: float, theta_ankle: float, flip: bool = False):
    """Return joint positions for a single leg."""
    hip = np.array([0.0, 0.0])
    # Knee position
    knee = hip + np.array([
        L_HIP_KNEE * np.sin(theta_hip),
        -L_HIP_KNEE * np.cos(theta_hip),
    ])

    # Shank orientation is hip angle plus knee flexion
    shank_angle = theta_hip + theta_knee
    ankle = knee + np.array([
        L_KNEE_ANKLE * np.sin(shank_angle),
        -L_KNEE_ANKLE * np.cos(shank_angle),
    ])

    # Foot orientation continues from shank
    foot_angle = shank_angle + theta_ankle
    foot = ankle + np.array([
        L_ANKLE_FOOT * np.sin(foot_angle),
        -L_ANKLE_FOOT * np.cos(foot_angle),
    ])

    if flip:
        hip[0] *= -1
        knee[0] *= -1
        ankle[0] *= -1
        foot[0] *= -1

    return hip, knee, ankle, foot


fig, ax = plt.subplots()
line, = ax.plot([], [], 'o-', lw=2)

ax.set_xlim(-2, 2)
ax.set_ylim(-2.5, 0.5)
ax.set_aspect('equal')
ax.grid(True)


def init():
    line.set_data([], [])
    return line,


def update(frame: int):
    i = frame % len(THETA_HIP)
    hip, knee, ankle, foot = compute_positions(
        THETA_HIP[i], THETA_KNEE[i], THETA_ANKLE[i], flip=True
    )
    xs = [hip[0], knee[0], ankle[0], foot[0]]
    ys = [hip[1], knee[1], ankle[1], foot[1]]
    line.set_data(xs, ys)
    return line,


ani = FuncAnimation(fig, update, frames=len(THETA_HIP), init_func=init, blit=True, repeat=True)
plt.show()
