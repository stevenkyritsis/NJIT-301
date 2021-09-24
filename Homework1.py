import math
import sympy

#1a
#What is the probability that a person will die between 60 and 70
t = 60
prob = (3*(10**-9)) * (t**2) * ((100 - t)**2)

print('60 ', prob, ' ')
t = 70
prob = (3*(10**-9)) * (t**2) * ((100 - t)**2)
print('70 ', prob, '\n')

#1b
# What is the probability that a person will die between 60 and 70, given that was alive at 60. 
