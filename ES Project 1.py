import numpy as np
import matplotlib.pyplot as plt

# Collected data on surface temperatures using thermometer. Held thermometer one meter off ground.
# Collected measured temperature in Celsius once the temperature reached a constant value.
t1_surface_temp = [["Water", 288], ["Grass", 293], ["Concrete", 303], ["Roads", 323]]
t2_surface_temp = [["Water", 288], ["Grass", 293], ["Concrete", 303], ["Roads", 323]]
t3_surface_temp = [["Water", 288], ["Grass", 293], ["Concrete", 303], ["Roads", 323]]

# Averages of the temperatures for each surface
water_avg = (t1_surface_temp[0][1] + t2_surface_temp[0][1] + t3_surface_temp[0][1]) / 3
grass_avg = (t1_surface_temp[1][1] + t2_surface_temp[1][1] + t3_surface_temp[1][1]) / 3
concrete_avg = (t1_surface_temp[2][1] + t2_surface_temp[2][1] + t3_surface_temp[2][1]) / 3
roads_avg = (t1_surface_temp[3][1] + t2_surface_temp[3][1] + t3_surface_temp[3][1]) / 3


# Function to calculate albedo with a greenhouse effect using Stefan-Boltzmann Law
def albedo(x):
    solar_constant = 1367
    delta = 0.0000000567
    return 1 - ((4 * delta * (x ** 4)) / (2 * solar_constant))

# Graph the function using the collected data
X = [albedo(water_avg), albedo(grass_avg), albedo(concrete_avg), albedo(roads_avg)]
Y = [water_avg, grass_avg, concrete_avg, roads_avg]

fig = plt.figure(figsize=(12,5))
ax = fig.add_subplot(121)
ax.plot(X, Y)
ax.set_title("Temperature Change as Albedo Increases")
plt.xlabel("Albedo")
plt.ylabel("Temperature (K)")
plt.show()

#Overall trend shows that as albedo increases, surface temperature decreases. As albedo decreases, surface temperatures increase.#
#Implications for increasing temperatures if global ice melts and there is construction of more manmade surfaces creating a positive feedback loop.

