#Plot different vectors on Bloch Sphere

"""
The general state of a qubit is represented by
|q> = A|0> + B|1>    where A and B belong to Complex Numbers.
Instead of having A and B be complex, we can confine them to the real numbers and add a term to tell us the relative phase between them:
|q> = A|0> + e^i(phi) B|1>    where A, B and phi belong to Real numbers.

From this we can describe the state of any qubit using the two variables (theta) and (phi)
A = cos(theta/2)   and   B = e^i(phi) sin(theta/2)
Using this calculate the value of (theta) and (phi) which is use to plot the vector in Bloch Sphere

|q> = cos(theta/2) |0> + e^i(phi) sin(theta/2) |1>.............equation(1)

To plot describe the co-ordinate as [theta, phi, radius of bloch sphere]
"""

from qiskit_textbook.widgets import plot_bloch_vector_spherical
from math import pi

"""
Plotting |0>
|0> = 1|0> + 0|1> . Comparing with equation(1) above we get (theta) = 0 and (phi) = 0
"""
c = [0,0,1]
plot_bloch_vector_spherical(c)

"""
Plotting |1>
|1> = 0|0> + 1|1> . Comparing with equation(1) above we get (theta) = pi and (phi) = 0
"""
a = [pi, 0, 1]
plot_bloch_vector_spherical(a)

"""
Plotting 1/sqrt(2)[|0> - i|1>]
Comparing we get (theta) = pi/2 and (phi) = -pi/2
"""
b = [pi/2, -pi/2, 1]
plot_bloch_vector_spherical(b)

"""
Plotting 1/sqrt(2)[i|0> + |1>]
Multiply it with a global factor e^i(alpha) to get the value of (theta) and (phi)
Comparing we get (theta) = pi/2 and (phi) = -pi/2
"""
d = [pi/2, -pi/2, 1]
plot_bloch_vector_spherical(d)