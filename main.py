"""
    main.py file
"""

import numpy as np
from activation_functions import my_activation_functions as af

print(af.linear_function(np.array([1, 2, 3, -4, 5, -6])))
print(af.relu(np.array([1, 2, 3, -4, 5, -6])))
print(af.elu(np.array([1, 2, 3, -4, 5, -6]), alpha=0.02))
print(af.leaky_relu(np.array([1, 2, 3, -4, 5, -6]), alpha=0.02))
print(af.sigmoid(np.array([1, 2, 3, -4, 5, -6])))
print(af.tanh(np.array([1, 2, 3, -4, 5, -6])))
