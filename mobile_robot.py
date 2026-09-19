import math
import matplotlib.pyplot as plt

def update_position(x,y,theta,velocity,dt,omega):
	next_x = x + velocity * math.cos(theta) * dt
	next_y = y + velocity * math.sin(theta) * dt
	next_theta = theta + omega * dt
	return next_x,next_y,next_theta

def main():
	x = 0.0
	y = 0.0
	theta = 0
	velocity = 1.0
	dt = 0.1
	duration = 2.0
	omega = 1

	if dt <= 0:
		raise ValueError("dt必须大于0")

	x_positions = []
	y_positions = []

	for i in range(int(duration/dt)):
		x_positions.append(x)
		y_positions.append(y)
		x,y,theta = update_position(x,y,theta,velocity,dt,omega)
		
	plt.plot(x_positions, y_positions, marker=".")
	plt.xlabel("x position (m)")
	plt.ylabel("y position (m)")
	plt.title("Mobile Robot Trajectory")
	plt.grid(True)
	plt.axis("equal")
	plt.savefig("trajectory_roundforward().png")
	plt.show()

main()
