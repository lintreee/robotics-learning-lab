import matplotlib.pyplot as plt

x_positions = [0, 1, 2, 3, 4]
y_positions = [0, 0.5, 1.2, 1.8, 2.0]

plt.plot(x_positions, y_positions, marker="o")
plt.xlabel("x position (m)")
plt.ylabel("y position (m)")
plt.title("Robot Trajectory")
plt.grid(True)
plt.axis("equal")
plt.savefig("robot_trajectory.png")
plt.show()
