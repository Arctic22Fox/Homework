from math import pi, tan, cos
# this was me to checking to see that the imports had imported correctly
print(pi)
print(tan)
print(cos)

# I then created variables to associate to the numbers in the equation
barrel = 1
distance = 0.5
elevation = 80
velocity = 44
acceleration = 9.81

theta = elevation * pi/180

print(theta)

y = barrel + 0.5

answer = barrel + distance * tan(theta) - (acceleration * distance ** 2) / (2*((velocity *cos(theta))**2))

print('The projectile is ' + str(answer) + 'm')

# actual answer

# from math import pi, tan, cos

# g = 9.81
# v0 = 44
# theta = 80 *pi/180
# x = 0.5
# y0 = 1

# y = y0 + x*tan(theta) - (g*x**2)/(2*((v0 * cos(theta))**2))

# print('Height: ', y, 'm')