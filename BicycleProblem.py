#necessary imports
import matplotlib.pyplot as plt
from vpython import *

#initial conditions and constants
velocity_initial = 4 #given
power = 400 #Average Power output of a cyclist, in watts
mass = 70 #kg
drag_coefficent = 0.5 #given
density = 1.225 #Density of Air, Found online, in kg/m^3
cross_sectional_area = 0.33 #m^2

#timing
dt = 0.1 #step
initial_time = 0
final_time = 200


#creating the data
time = []
velocity_out = []
velocity_out_drag = []

TotalSteps = (final_time - initial_time) / dt

def Bicycle():
    
    #setting the initial values
    time.append(0)
    velocity_out.append(velocity_initial)        
    velocity_out_drag.append(velocity_initial)

    #iterating through the steps
    for t in range(1,int(TotalSteps)):
        #calculating time step
        time.append(time[t-1] + dt)
        
        #calculating and adding velocity step with no air resistance
        motion_value = velocity_out[t-1] + power / (mass*velocity_out[t-1]) * dt
        velocity_out.append(motion_value)
        
         #calculating and adding velocity step with air resistance
        air_drag_value = velocity_out_drag[t-1] + power / (mass*velocity_out_drag[t-1]) * dt - drag_coefficent * density * cross_sectional_area * velocity_out_drag[t-1]**2 * dt / mass
        velocity_out_drag.append(air_drag_value)

#calling function
Bicycle()


#configuring final figure  
figure = plt.figure(figsize=(4, 4), dpi=80)

#plotting data
plt.plot(time, velocity_out_drag, linestyle='dashed', label='With air resistance')
plt.plot(time, velocity_out,label='No air resistance')

#setting limits on figure
plt.xlim(initial_time,final_time)
plt.ylim(0,50)

#setting the ticks
plt.xticks(np.arange(0,201,50))

#axis labels
plt.xlabel("time (s)")
plt.ylabel("velocity (m/s)")

#labels on the lines 
plt.text(80,7,'With air resistance')
plt.text(10,35,'No air resistance')

#title of figure
plt.title("Bicycle simulation: velocity vs. time")

#show the figure (for testing purposes)
plt.show()

#exporting figure
figure.savefig('Computational Physics HW - Figure 2.2.png')
