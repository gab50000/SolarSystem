import numpy as np
import re

def get_coordinates_velocities(filename):
    with open(filename, "r") as f:
        x = f.read()
        data, = re.findall("\$\$SOE(.*)\$\$EOE", x, flags=re.DOTALL)
        pos = map(float, data.splitlines()[-3].split())
        vel = map(float, data.splitlines()[-2].split())
        return pos, vel

