import numpy as np
import matplotlib.pyplot as plt
import orbit
from celluloid import Camera


# Set an initial velocity and position for comet
r0 = 1
v0 = 6.28
comet_orbit = orbit.orbit_traj(r0,v0,200,0.01,3)

# Separate the result tuple
thplot = comet_orbit[0]
rplot = comet_orbit[1]


fig = plt.figure()
camera = Camera(fig)


for i in range(200):
    plt.scatter(rplot[i]*np.cos(thplot[i]),rplot[i]*np.sin(thplot[i]), c = 'r')
    plt.scatter(0,0, c = 'y')
    camera.snap()
animation = camera.animate()
plt.show()




