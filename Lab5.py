import numpy as np
import matplotlib.pyplot as plt
import orbit
from celluloid import Camera

# Part 2 - Mackenzie Kuntz
# Set an initial velocity and position for comet
r0 = 1
v0 = 6.28
comet_orbit = orbit.orbit_traj(r0,v0,200,0.01,3)

# Separate the result tuple
thplot = comet_orbit[0]
rplot = comet_orbit[1]

#Animate plot of comet orbiting the Sun
fig = plt.figure()
camera = Camera(fig)
plt.ylabel('Position from the Sun in the y-direction (AU)')
plt.xlabel('Position from the Sun in the x-direction (AU)')
plt.title('Comet Orbit Trajectory with Initial Velocity 6.28 Au/year and an\n Initial Position 1 AU')
plt.scatter(0,0, c = 'y', label = "Sun")
plt.scatter(rplot[0]*np.cos(thplot[0]),rplot[0]*np.sin(thplot[0]), c = 'r', label = "Comet")

for i in range(200):
    plt.scatter(rplot[i]*np.cos(thplot[i]),rplot[i]*np.sin(thplot[i]), c = 'r')
    plt.scatter(0,0, c = 'y')
    camera.snap()
animation = camera.animate()
plt.legend()
#plt.show()

#Save animation
animation.save('Group10_Lab5_comet.gif')




