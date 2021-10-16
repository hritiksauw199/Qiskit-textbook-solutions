# Plot different vectors on Bloch Sphere

"""
See the calculation file for detailed explanation
"""

from qiskit_textbook.widgets import plot_bloch_vector_spherical
from math import pi

"""
Plotting |0>
"""
c = [0,0,1]
plot_bloch_vector_spherical(c)

"""
Plotting |1>
"""
a = [pi, 0, 1]
plot_bloch_vector_spherical(a)

"""
Plotting 1/sqrt(2)[|0> - i|1>]
"""
b = [pi/2, -pi/2, 1]
plot_bloch_vector_spherical(b)

"""
Plotting 1/sqrt(2)[i|0> + |1>]
"""
d = [pi/2, -pi/2, 1]
plot_bloch_vector_spherical(d)


"""
Plotting 1/sqrt(2)[|0> + |1>]
"""
e = [pi/2, 0, 1]
plot_bloch_vector_spherical(e)