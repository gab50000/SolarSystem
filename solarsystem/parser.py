import numpy as np
import re
import ipdb

def get_coordinates_velocities(filename):
    with open(filename, "r") as f:
        x = f.read()
        data, = re.findall("\$\$SOE(.*)\$\$EOE", x, flags=re.DOTALL)
        pos = map(float, data.splitlines()[-3].split())
        vel = map(float, data.splitlines()[-2].split())
        return pos, vel


def get_masses(filename):
    with open(filename, "r") as f:
        for line in f:
            if "Mass" in line:
                try:
                    mass = re.findall("mass[^\=]*\=\s*(\d*\.\d+)", line, flags=re.IGNORECASE)[0]
                except:
                    ipdb.set_trace()
                break
        else:
            with open(filename, "r") as f:
                x = f.read()
                try:
                    mass = re.findall("mass:\s*([^\s]+)", x, flags=re.IGNORECASE)[0]
                except:
                    ipdb.set_trace()
                mass = float(mass)
    return mass
         
